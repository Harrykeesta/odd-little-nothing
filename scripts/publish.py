"""Owner issue -> validated local image + index. No credentials in the reader."""
import io, json, os, re, urllib.request, urllib.parse
from pathlib import Path
from PIL import Image
Image.MAX_IMAGE_PIXELS = 20_000_000

def parse(event, owner):
    issue = event['issue']
    if issue['user']['login'] != owner or event['sender']['login'] != owner:
        raise ValueError('Only the owner may publish')
    title = issue['title']
    if not title.startswith('[comic] ') or not title[8:].strip():
        raise ValueError('Use the comic template and add a title')
    body = issue.get('body') or ''
    urls = re.findall(r'https://(?:github\.com/user-attachments/assets/|user-images\.githubusercontent\.com/)[^\s)<>"\]]+', body)
    if len(urls) != 1: raise ValueError('Attach exactly one image')
    transcript = body.partition('### Transcript')[2].strip()
    if not transcript or len(transcript)>3000: raise ValueError('Transcript required, maximum 3000 characters')
    return issue, title[8:].strip()[:100], urls[0], transcript

def allowed(url):
    p=urllib.parse.urlsplit(url)
    return p.scheme=='https' and p.hostname in {'github.com','user-images.githubusercontent.com','private-user-images.githubusercontent.com','github-production-user-asset-6210df.s3.amazonaws.com'} and not p.username

class SafeRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl):
        if not allowed(newurl): raise ValueError('Unsupported attachment redirect')
        return super().redirect_request(req,fp,code,msg,headers,newurl)

def publish(event, owner, root=Path('.'), download=None):
    issue,title,url,alt=parse(event,owner)
    comics=json.loads((root/'comics.json').read_text())
    identifier='issue-'+str(int(issue['number']))
    if any(c['id']==identifier for c in comics): return False
    if download is None:
        with urllib.request.build_opener(SafeRedirect).open(url,timeout=30) as response:
            raw=response.read(10_000_001)
    else: raw=download(url)
    if len(raw)>10_000_000: raise ValueError('Image exceeds 10 MB')
    with Image.open(io.BytesIO(raw)) as im:
        if im.format not in {'PNG','JPEG','WEBP'}: raise ValueError('Unsupported image type')
        im.load()
        if im.width<300 or im.height<200: raise ValueError('Image too small')
        im=im.convert('RGB');im.thumbnail((1600,1600))
        # Fresh encoding omits source EXIF and personal metadata.
        im.save(root/f'site/comics/{identifier}.webp','WEBP',quality=82)
    comics.append({'id':identifier,'title':title,'image':f'comics/{identifier}.webp','alt':alt,'captions':[], 'width':im.width, 'height':im.height})
    target=root/'comics.json';tmp=target.with_suffix('.tmp');tmp.write_text(json.dumps(comics,indent=2)+'\n');tmp.replace(target)
    return True

if __name__=='__main__':
    publish(json.loads(Path(os.environ['GITHUB_EVENT_PATH']).read_text()),os.environ['GITHUB_REPOSITORY_OWNER'])

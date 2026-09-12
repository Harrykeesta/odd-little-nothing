import copy, io, json, tempfile, unittest
from pathlib import Path
from PIL import Image
from publish import publish, parse
class Publishing(unittest.TestCase):
 def test_owner_validation_and_import(self):
  event={'sender':{'login':'anon'},'issue':{'user':{'login':'anon'},'number':7,'title':'[comic] Hi <script>','body':'### Comic\n![image](https://github.com/user-attachments/assets/test)\n### Transcript\nA blob.'}}
  bad=copy.deepcopy(event);bad['sender']['login']='stranger'
  with self.assertRaises(ValueError):parse(bad,'anon')
  buf=io.BytesIO();Image.new('RGB',(600,600),'white').save(buf,'PNG')
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);(root/'site/comics').mkdir(parents=True);(root/'comics.json').write_text('[]')
   self.assertTrue(publish(event,'anon',root,lambda _:buf.getvalue()))
   self.assertFalse(publish(event,'anon',root,lambda _:buf.getvalue()))
   self.assertEqual(len(json.loads((root/'comics.json').read_text())),1)
   self.assertTrue((root/'site/comics/issue-7.webp').exists())
 def test_non_image(self):
  event={'sender':{'login':'anon'},'issue':{'user':{'login':'anon'},'number':7,'title':'[comic] Hi','body':'https://github.com/user-attachments/assets/test\n### Transcript\nA blob.'}}
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);(root/'comics.json').write_text('[]')
   with self.assertRaises(Exception):publish(event,'anon',root,lambda _:b'<script>')
   self.assertEqual((root/'comics.json').read_text(),'[]')
if __name__=='__main__':unittest.main()

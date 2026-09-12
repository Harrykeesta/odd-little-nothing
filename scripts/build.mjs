import fs from 'node:fs';
const comics=JSON.parse(fs.readFileSync('comics.json','utf8'));
const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
if(!comics.length)throw Error('At least one comic required');
const ids=new Set();
for(const c of comics){if(!/^[a-z0-9-]+$/.test(c.id)||ids.has(c.id))throw Error('Invalid/duplicate ID');ids.add(c.id);if(!/^comics\/[a-z0-9-]+\.webp$/.test(c.image)||!fs.existsSync('site/'+c.image))throw Error('Missing/invalid artwork: '+c.image);if(!c.title||!c.alt||!Array.isArray(c.captions)||![0,3].includes(c.captions.length))throw Error('Invalid comic');}
function page(c,i){const link=(j,rel,arrow,label)=>comics[j]?`<a rel="${rel}" href="${comics[j].id}.html" aria-label="${label}">${arrow}</a>`:`<span class="edge" aria-hidden="true">${arrow}</span>`;return `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="${esc(c.alt)}"><meta name="referrer" content="no-referrer"><title>${esc(c.title)} — odd little nothing</title><link rel="stylesheet" href="style.css"><script src="reader.js" defer></script></head><body><header><a href="index.html">odd little nothing<span aria-hidden="true" style="color:#777">.</span></a><span>a comic, occasionally</span></header><main><div class="eyebrow">NO. ${esc(c.id)}</div><h1>${esc(c.title)}</h1><figure class="${c.captions.length ? 'sample' : ''}"><img src="${esc(c.image)}" alt="${esc(c.alt)}" width="${c.width||1254}" height="${c.height||1254}" fetchpriority="high"><figcaption>${c.captions.map(t=>`<p>${esc(t)}</p>`).join('')}</figcaption></figure><nav aria-label="Comic navigation">${link(i-1,'prev','←','Older comic')}<small>${i+1} / ${comics.length}</small>${link(i+1,'next','→','Newer comic')}</nav></main><footer>by nobody in particular</footer></body></html>`}
comics.forEach((c,i)=>fs.writeFileSync(`site/${c.id}.html`,page(c,i)));
fs.writeFileSync('site/index.html',page(comics.at(-1),comics.length-1));
fs.writeFileSync('site/.nojekyll','');
console.log(`Built ${comics.length} comics. Static HTML, no reader dependencies.`);
fs.rmSync('dist',{recursive:true,force:true});fs.cpSync('site','dist',{recursive:true});

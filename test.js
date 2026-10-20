const fs=require('fs');const h=fs.readFileSync('index.html','utf8');const js=h.match(/<script>([\s\S]*)<\/script>/)[1];new Function(js);
const d=JSON.parse(fs.readFileSync('questions/2026-10-21.json'));if(d.questions.length!==10)throw'n';d.questions.forEach(q=>{if(q.options.length!==4||!(q.answer>=0&&q.answer<4))throw q.id});console.log('test ok')
const iv=JSON.parse(fs.readFileSync('interview.json'));if(iv.items.length!==5)throw'iv';if(!h.includes('showInterview')||!h.includes('speechSynthesis'))throw'feat';console.log('interview ok')

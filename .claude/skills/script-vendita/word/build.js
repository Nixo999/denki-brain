const fs = require('fs');
const path = require('path');
const { build, Packer } = require('./build-lib.js');
const OUT = '/Users/patricksappa/Desktop/denki-brain/02-Sales/script';
(async () => {
  for (const f of ['content-a.js', 'content-b.js', 'content-c.js', 'content-d.js']) {
    const c = require('./' + f);
    const doc = build(c);
    const buf = await Packer.toBuffer(doc);
    fs.writeFileSync(path.join(OUT, c.file), buf);
    console.log(c.file, buf.length + ' byte');
  }
})();

const d = require('docx');
const {Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType,
       ShadingType, BorderStyle, AlignmentType, HeadingLevel, Footer, PageNumber,
       TableLayoutType} = d;

const FONT = 'Arial';
const INK = '111111', SOFT = '595959', MID = '333333';
const BOX = 'F2F2F2', HEAD = 'E4E4E4';

// **grassetto** e *corsivo* dentro una stringa
function rich(text, base = {}) {
  const out = [];
  const re = /(\*\*[^*]+\*\*|\*[^*]+\*)/g;
  let last = 0, m;
  while ((m = re.exec(text)) !== null) {
    if (m.index > last) out.push(new TextRun({ ...base, text: text.slice(last, m.index) }));
    const tok = m[0];
    if (tok.startsWith('**')) out.push(new TextRun({ ...base, text: tok.slice(2, -2), bold: true }));
    else out.push(new TextRun({ ...base, text: tok.slice(1, -1), italics: true }));
    last = m.index + tok.length;
  }
  if (last < text.length) out.push(new TextRun({ ...base, text: text.slice(last) }));
  return out;
}

const P = (text, o = {}) => new Paragraph({
  spacing: { before: o.before ?? 0, after: o.after ?? 120, line: 264 },
  indent: o.indent,
  alignment: o.alignment,
  children: rich(text, { font: FONT, size: o.size ?? 20, color: o.color ?? MID, bold: o.bold, italics: o.italics }),
});

const H = (text, tag) => [
  new Paragraph({
    spacing: { before: 320, after: 0 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: INK, space: 4 } },
    children: [new TextRun({ text: text.toUpperCase(), font: FONT, size: 22, bold: true, color: INK, characterSpacing: 20 })],
  }),
  ...(tag ? [new Paragraph({
    spacing: { before: 60, after: 140 },
    children: [new TextRun({ text: tag, font: FONT, size: 17, italics: true, color: SOFT })],
  })] : [new Paragraph({ spacing: { before: 0, after: 100 }, children: [] })]),
];

// battuta parlata: riquadro grigio in tabella (l'ombreggiatura di paragrafo
// non regge fuori da Word, quella di cella sì)
const WIDTH = 9740;
const SAY = (lines) => [
  new Table({
    columnWidths: [WIDTH],
    layout: TableLayoutType.FIXED,
    width: { size: WIDTH, type: WidthType.DXA },
    borders: {
      top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE },
      right: { style: BorderStyle.NONE },
      left: { style: BorderStyle.SINGLE, size: 18, color: INK },
      insideHorizontal: { style: BorderStyle.NONE }, insideVertical: { style: BorderStyle.NONE },
    },
    rows: [new TableRow({
      children: [new TableCell({
        width: { size: WIDTH, type: WidthType.DXA },
        shading: { type: ShadingType.CLEAR, fill: BOX, color: 'auto' },
        margins: { top: 140, bottom: 140, left: 220, right: 220 },
        children: lines.map((ln, i) => new Paragraph({
          spacing: { before: i === 0 ? 0 : 80, after: 0, line: 288 },
          children: ln.startsWith('(')
            ? [new TextRun({ text: ln, font: FONT, size: 19, italics: true, color: SOFT })]
            : [new TextRun({ text: '«' + ln + '»', font: FONT, size: 22, bold: true, color: '000000' })],
        })),
      })],
    })],
  }),
  new Paragraph({ spacing: { after: 140 }, children: [] }),
];

// nota operativa: riga con filetto sopra
const NOTE = (text) => new Paragraph({
  spacing: { before: 60, after: 160, line: 264 },
  indent: { left: 240 },
  children: rich(text, { font: FONT, size: 18, color: SOFT }),
});

const cell = (children, o = {}) => new TableCell({
  width: { size: o.w, type: WidthType.DXA },
  shading: o.fill ? { type: ShadingType.CLEAR, fill: o.fill, color: 'auto' } : undefined,
  margins: { top: 80, bottom: 80, left: 120, right: 120 },
  children,
});

const TBL = (head, rows, widths) => new Table({
  columnWidths: widths,
  layout: TableLayoutType.FIXED,
  width: { size: widths.reduce((a, b) => a + b, 0), type: WidthType.DXA },
  borders: {
    top: { style: BorderStyle.SINGLE, size: 4, color: 'BFBFBF' },
    bottom: { style: BorderStyle.SINGLE, size: 4, color: 'BFBFBF' },
    left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE },
    insideHorizontal: { style: BorderStyle.SINGLE, size: 2, color: 'D9D9D9' },
    insideVertical: { style: BorderStyle.NONE },
  },
  rows: [
    new TableRow({
      tableHeader: true,
      children: head.map((h, i) => cell([new Paragraph({
        spacing: { after: 0 },
        children: [new TextRun({ text: h.toUpperCase(), font: FONT, size: 16, bold: true, color: INK, characterSpacing: 14 })],
      })], { w: widths[i], fill: HEAD })),
    }),
    ...rows.map(r => new TableRow({
      children: r.map((c, i) => cell([new Paragraph({
        spacing: { after: 0, line: 252 },
        children: rich(c, { font: FONT, size: 18, color: MID }),
      })], { w: widths[i] })),
    })),
  ],
});

function render(block) {
  switch (block.t) {
    case 'h': return H(block.text, block.tag);
    case 'p': return [P(block.text)];
    case 'say': return SAY(block.lines);
    case 'note': return [NOTE(block.text)];
    case 'obj': return [
      new Paragraph({
        spacing: { before: 220, after: 60 },
        children: [new TextRun({ text: '«' + block.q + '»', font: FONT, size: 20, bold: true, color: INK })],
      }),
      ...SAY(block.lines),
      ...(block.note ? [NOTE(block.note)] : []),
    ];
    case 'table': return [TBL(block.head, block.rows, block.widths), P('', { after: 60 })];
    case 'list': return block.items.map((it, i) => new Paragraph({
      spacing: { after: 80, line: 264 },
      indent: { left: 340, hanging: 220 },
      children: [
        new TextRun({ text: (block.ordered ? (i + 1) + '.' : '□') + '  ', font: FONT, size: 20, color: INK, bold: true }),
        ...rich(it, { font: FONT, size: 20, color: MID }),
      ],
    }));
    case 'break': return [new Paragraph({ children: [new d.PageBreak()] })];
    default: throw new Error('blocco sconosciuto: ' + block.t);
  }
}

function build({ title, product, objective, blocks }) {
  const children = [
    new Paragraph({
      spacing: { after: 40 },
      children: [new TextRun({ text: 'DENKICODE · SCRIPT PER LE CHIAMATE', font: FONT, size: 16, bold: true, color: SOFT, characterSpacing: 30 })],
    }),
    new Paragraph({
      spacing: { after: 60 },
      children: [new TextRun({ text: title, font: FONT, size: 36, bold: true, color: INK })],
    }),
    new Paragraph({
      spacing: { after: 200 },
      border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: INK, space: 6 } },
      children: [new TextRun({ text: product, font: FONT, size: 19, color: SOFT })],
    }),
    new Table({
      columnWidths: [WIDTH],
      layout: TableLayoutType.FIXED,
      width: { size: WIDTH, type: WidthType.DXA },
      borders: {
        top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE },
        left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE },
        insideHorizontal: { style: BorderStyle.NONE }, insideVertical: { style: BorderStyle.NONE },
      },
      rows: [new TableRow({
        children: [new TableCell({
          width: { size: WIDTH, type: WidthType.DXA },
          shading: { type: ShadingType.CLEAR, fill: HEAD, color: 'auto' },
          margins: { top: 180, bottom: 180, left: 220, right: 220 },
          children: [new Paragraph({
            spacing: { after: 0, line: 276 },
            children: rich(objective, { font: FONT, size: 20, color: INK }),
          })],
        })],
      })],
    }),
    new Paragraph({ spacing: { after: 160 }, children: [] }),
    ...blocks.flatMap(render),
  ];

  return new Document({
    creator: 'DenkiCode',
    description: 'Script telefonico DenkiCode - versione del 31/08/2026, da correggere dopo le chiamate',
    title,
    styles: { default: { document: { run: { font: FONT, size: 20, color: MID } } } },
    sections: [{
      properties: { page: { margin: { top: 1000, right: 1080, bottom: 1000, left: 1080 } } },
      footers: {
        default: new Footer({
          children: [new Paragraph({
            alignment: AlignmentType.CENTER,
            spacing: { before: 200 },
            children: [new TextRun({
              children: ['DenkiCode · uso interno · versione del 31/08/2026 · quello fra virgolette si dice, il resto è per capire · pag. ', PageNumber.CURRENT],
              font: FONT, size: 15, color: SOFT,
            })],
          })],
        }),
      },
      children,
    }],
  });
}

module.exports = { build, Packer };

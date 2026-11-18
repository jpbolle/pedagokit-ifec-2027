// Extrait le texte d'un PDF sur Mac, sans rien installer (PDFKit, intégré à macOS).
// Usage : osascript -l JavaScript harnais/outils/pdf_en_texte.js "<chemin absolu du PDF>" > sortie.txt
ObjC.import('PDFKit');
function run(argv) {
  var doc = $.PDFDocument.alloc.initWithURL($.NSURL.fileURLWithPath(argv[0]));
  return doc.string.js;
}

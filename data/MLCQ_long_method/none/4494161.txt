   static private String getSwapInfoScript() {
      String functionText = "  function iaf(txt) {\n" +
            "    var aff=txt.replace( /" + AFFIRMED + "/g,\"<br><h3>Affirmed</h3>\" );\n" +
            "    var neg=aff.replace( /" + NEGATED + "/g,\"<br><h3>Negated</h3>\" );\n" +
            "    var unc=neg.replace( /" + UNCERTAIN + "/g,\"<br><h3>Uncertain</h3>\" );\n" +
            "    var unn=unc.replace( /" + UNCERTAIN_NEGATED + "/g,\"<br><h3>Uncertain, Negated</h3>\" );\n" +
            "    var gnr=unn.replace( /" + GENERIC + "/g,\"\" );\n" +

            "    var wik1=gnr.replace( /" + WIKI_BEGIN
            + "/g,\"<a href=\\\"https://vsearch.nlm.nih.gov/vivisimo/cgi-bin/query-meta?v%3Aproject=medlineplus&v%3Asources=medlineplus-bundle&query=\" );\n" +
            "    var wik2=wik1.replace( /" + WIKI_CENTER + "/g,\"\\\" target=\\\"_blank\\\">\" );\n" +
            "    var wik3=wik2.replace( /" + WIKI_END + "/g,\"</a>\" );\n";

      String previousCode = "wik3";
      for ( SemanticMarkup markup : SemanticMarkup.values() ) {
         functionText += createSemanticReplacements( markup, previousCode );
         previousCode = markup.getEncoding()
               .toLowerCase();
      }
      functionText +=
            "    var spc=_unk_.replace( /" + SPACER + "/g,\"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\" );\n" +
                  "    var prf1=spc.replace( /\\[/g,\"<i>\" );\n" +
                  "    var prf2=prf1.replace( /\\]/g,\"</i>\" );\n" +
                  "    var nl=prf2.replace( /" + NEWLINE + "/g,\"<br>\" );\n" +
                  "    document.getElementById(\"ia\").innerHTML = nl;\n" +
                  "  }\n";
      return functionText;
   }
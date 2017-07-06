(function(){"use strict";CodeMirror.switchSlackMode=function(editor,mode){var type_map={c:["clike","text/x-csrc"],clojure:["clojure","text/x-clojure"],coffeescript:["coffeescript","text/x-coffeescript"],commonlisp:["commonlisp","text/x-commonlisp"],cpp:["clike","text/x-c++src"],crystal:["crystal","text/x-crystal"],csharp:["clike","text/x-csharp"],css:["css","text/css"],cypher:["cypher","application/x-cypher-query"],d:["d","text/x-d"],dart:["dart","text/x-dart"],diff:["diff","text/x-diff"],dockerfile:["dockerfile","text/x-dockerfile"],erlang:["erlang","text/x-erlang"],fortran:["fortran","text/x-fortran"],fsharp:["mllike","text/x-fsharp"],gherkin:["gherkin","text/x-feature"],go:["go","text/x-go"],groovy:["groovy","text/x-groovy"],handlebars:["handlebars","text/x-handlebars"],haskell:["haskell","text/x-haskell"],haxe:["haxe","text/x-haxe"],html:["htmlmixed","text/html"],java:["clike","text/x-java"],javascript:["javascript","text/javascript"],json:["javascript","application/json"],julia:["julia","text/x-julia"],kotlin:["clike","text/x-kotlin"],latex:["stex","text/x-stex"],lisp:["commonlisp","text/x-lisp"],lua:["lua","text/x-lua"],markdown:["markdown","text/x-markdown"],mathematica:["mathematica","text/x-mathematica"],matlab:["octave","text/x-octave"],mumps:["mumps","text/x-mumps"],mysql:["sql","text/x-mysql"],objc:["clike","text/x-objectivec"],ocaml:["mllike","text/x-ocaml"],pascal:["pascal","text/x-pascal"],perl:["perl","text/x-perl"],php:["php","application/x-httpd-php"],pig:["pig","text/x-pig"],powershell:["powershell","text/x-powershell"],puppet:["puppet","text/x-puppet"],python:["python","text/x-python"],r:["r","text/x-rsrc"],ruby:["ruby","text/x-ruby"],rust:["rust","text/x-rustsrc"],sass:["sass","text/x-sass"],scala:["clike","text/x-scala"],scheme:["scheme","text/x-scheme"],shell:["shell","text/x-sh"],smalltalk:["smalltalk","text/x-stsrc"],sql:["sql","text/x-sql"],swift:["swift","text/x-swift"],vb:["vb","text/x-vb"],vbscript:["vbscript","text/vbscript"],velocity:["velocity","text/x-velocity"],verilog:["verilog","text/x-verilog"],xml:["xml","text/xml"],yaml:["yaml","text/x-yaml"]};if(type_map[mode]){editor.setOption("mode",type_map[mode][1]);CodeMirror.autoLoadMode(editor,type_map[mode][0])}else{editor.setOption("mode",null)}};function codemirrorMap(file){switch(file){case"apl":return cdn_url+"/2fad/js/libs/codemirror/apl.js";case"asciiarmor":return cdn_url+"/b1e0/js/libs/codemirror/asciiarmor.js";case"asn.1":return cdn_url+"/bb21b/js/libs/codemirror/asn.1.js";case"asterisk":return cdn_url+"/8ea0/js/libs/codemirror/asterisk.js";case"brainfuck":return cdn_url+"/8ae8/js/libs/codemirror/brainfuck.js";case"clike":return cdn_url+"/8b781/js/libs/codemirror/clike.js";case"clojure":return cdn_url+"/b832/js/libs/codemirror/clojure.js";case"cmake":return cdn_url+"/f825/js/libs/codemirror/cmake.js";case"cobol":return cdn_url+"/e457/js/libs/codemirror/cobol.js";case"coffeescript":return cdn_url+"/23f6/js/libs/codemirror/coffeescript.js";case"commonlisp":return cdn_url+"/f435/js/libs/codemirror/commonlisp.js";case"css":return cdn_url+"/808c/js/libs/codemirror/css.js";case"crystal":return cdn_url+"/fb01/js/libs/codemirror/crystal.js";case"cypher":return cdn_url+"/1ea3/js/libs/codemirror/cypher.js";case"d":return cdn_url+"/1cda/js/libs/codemirror/d.js";case"dart":return cdn_url+"/0554/js/libs/codemirror/dart.js";case"diff":return cdn_url+"/5f39/js/libs/codemirror/diff.js";case"django":return cdn_url+"/e92ce/js/libs/codemirror/django.js";case"dockerfile":return cdn_url+"/d952/js/libs/codemirror/dockerfile.js";case"dtd":return cdn_url+"/4d46/js/libs/codemirror/dtd.js";case"dylan":return cdn_url+"/e5d66/js/libs/codemirror/dylan.js";case"ebnf":return cdn_url+"/bc88/js/libs/codemirror/ebnf.js";case"ecl":return cdn_url+"/68f2/js/libs/codemirror/ecl.js";case"eiffel":return cdn_url+"/37d8/js/libs/codemirror/eiffel.js";case"elm":return cdn_url+"/b2265/js/libs/codemirror/elm.js";case"erlang":return cdn_url+"/04323/js/libs/codemirror/erlang.js";case"factor":return cdn_url+"/eddb/js/libs/codemirror/factor.js";case"forth":return cdn_url+"/346cc/js/libs/codemirror/forth.js";case"fortran":return cdn_url+"/4cd8/js/libs/codemirror/fortran.js";case"gas":return cdn_url+"/fb60/js/libs/codemirror/gas.js";case"gfm":return cdn_url+"/8a51/js/libs/codemirror/gfm.js";case"gherkin":return cdn_url+"/1731/js/libs/codemirror/gherkin.js";case"go":return cdn_url+"/1d8f/js/libs/codemirror/go.js";case"groovy":return cdn_url+"/c505/js/libs/codemirror/groovy.js";case"haml":return cdn_url+"/b47a/js/libs/codemirror/haml.js";case"handlebars":return cdn_url+"/dd1c9/js/libs/codemirror/handlebars.js";case"haskell":return cdn_url+"/4890/js/libs/codemirror/haskell.js";case"haxe":return cdn_url+"/f022/js/libs/codemirror/haxe.js";case"htmlembedded":return cdn_url+"/462e/js/libs/codemirror/htmlembedded.js";case"htmlmixed":return cdn_url+"/21a23/js/libs/codemirror/htmlmixed.js";case"http":return cdn_url+"/b911/js/libs/codemirror/http.js";case"idl":return cdn_url+"/eff9/js/libs/codemirror/idl.js";case"jade":return cdn_url+"/ab45e/js/libs/codemirror/jade.js";case"javascript":return cdn_url+"/2929/js/libs/codemirror/javascript.js";case"jinja2":return cdn_url+"/d7c1/js/libs/codemirror/jinja2.js";case"julia":return cdn_url+"/73b5/js/libs/codemirror/julia.js";case"livescript":return cdn_url+"/42fb/js/libs/codemirror/livescript.js";case"lua":return cdn_url+"/d291/js/libs/codemirror/lua.js";case"markdown":return cdn_url+"/df31/js/libs/codemirror/markdown.js";case"mathematica":return cdn_url+"/84ed/js/libs/codemirror/mathematica.js";case"mirc":return cdn_url+"/bdf0/js/libs/codemirror/mirc.js";case"mllike":return cdn_url+"/09a3/js/libs/codemirror/mllike.js";case"modelica":return cdn_url+"/08a91/js/libs/codemirror/modelica.js";case"mscgen":return cdn_url+"/01df/js/libs/codemirror/mscgen.js";case"mumps":return cdn_url+"/b08c/js/libs/codemirror/mumps.js";case"nginx":return cdn_url+"/66fe/js/libs/codemirror/nginx.js";case"nsis":return cdn_url+"/3321/js/libs/codemirror/nsis.js";case"ntriples":return cdn_url+"/3946/js/libs/codemirror/ntriples.js";case"octave":return cdn_url+"/cf67/js/libs/codemirror/octave.js";case"oz":return cdn_url+"/5332/js/libs/codemirror/oz.js";case"pascal":return cdn_url+"/df9e/js/libs/codemirror/pascal.js";case"pegjs":return cdn_url+"/9c2f/js/libs/codemirror/pegjs.js";case"perl":return cdn_url+"/3f4e/js/libs/codemirror/perl.js";case"php":return cdn_url+"/a793e/js/libs/codemirror/php.js";case"pig":return cdn_url+"/938a/js/libs/codemirror/pig.js";case"powershell":return cdn_url+"/f9f57/js/libs/codemirror/powershell.js";case"properties":return cdn_url+"/2add4/js/libs/codemirror/properties.js";case"puppet":return cdn_url+"/753b2/js/libs/codemirror/puppet.js";case"python":return cdn_url+"/7291f/js/libs/codemirror/python.js";case"q":return cdn_url+"/6912/js/libs/codemirror/q.js";case"r":return cdn_url+"/d35d/js/libs/codemirror/r.js";case"rpm":return cdn_url+"/4b80/js/libs/codemirror/rpm.js";case"rst":return cdn_url+"/4792/js/libs/codemirror/rst.js";case"ruby":return cdn_url+"/29bc/js/libs/codemirror/ruby.js";case"rust":return cdn_url+"/2ca3/js/libs/codemirror/rust.js";case"sass":return cdn_url+"/5362/js/libs/codemirror/sass.js";case"scheme":return cdn_url+"/ff25/js/libs/codemirror/scheme.js";case"shell":return cdn_url+"/0103/js/libs/codemirror/shell.js";case"sieve":return cdn_url+"/774e/js/libs/codemirror/sieve.js";case"slim":return cdn_url+"/347f/js/libs/codemirror/slim.js";case"smalltalk":return cdn_url+"/0918/js/libs/codemirror/smalltalk.js";case"smarty":return cdn_url+"/71e81/js/libs/codemirror/smarty.js";case"solr":return cdn_url+"/c6f4/js/libs/codemirror/solr.js";case"soy":return cdn_url+"/0ef7/js/libs/codemirror/soy.js";case"sparql":return cdn_url+"/755b4/js/libs/codemirror/sparql.js";case"spreadsheet":return cdn_url+"/d1c6/js/libs/codemirror/spreadsheet.js";case"sql":return cdn_url+"/39a2/js/libs/codemirror/sql.js";case"stex":return cdn_url+"/5473/js/libs/codemirror/stex.js";case"stylus":return cdn_url+"/2895/js/libs/codemirror/stylus.js";case"swift":return cdn_url+"/e824/js/libs/codemirror/swift.js";case"tcl":return cdn_url+"/70804/js/libs/codemirror/tcl.js";case"textile":return cdn_url+"/ac044/js/libs/codemirror/textile.js";case"tiddlywiki":return cdn_url+"/3e53/js/libs/codemirror/tiddlywiki.js";case"tiki":return cdn_url+"/bf398/js/libs/codemirror/tiki.js";case"toml":return cdn_url+"/4596/js/libs/codemirror/toml.js";case"tornado":return cdn_url+"/cd62/js/libs/codemirror/tornado.js";case"troff":return cdn_url+"/27590/js/libs/codemirror/troff.js";case"ttcn":return cdn_url+"/cc5f1/js/libs/codemirror/ttcn.js";case"ttcn-cfg":return cdn_url+"/d168/js/libs/codemirror/ttcn-cfg.js";case"turtle":return cdn_url+"/27a1/js/libs/codemirror/turtle.js";case"twig":return cdn_url+"/037e/js/libs/codemirror/twig.js";case"vb":return cdn_url+"/81fe/js/libs/codemirror/vb.js";case"vbscript":return cdn_url+"/6553/js/libs/codemirror/vbscript.js";case"velocity":return cdn_url+"/192e/js/libs/codemirror/velocity.js";case"verilog":return cdn_url+"/de6e2/js/libs/codemirror/verilog.js";case"vhdl":return cdn_url+"/698a/js/libs/codemirror/vhdl.js";case"vue":return cdn_url+"/8d28/js/libs/codemirror/vue.js";case"xml":return cdn_url+"/8636/js/libs/codemirror/xml.js";case"xquery":return cdn_url+"/f72a/js/libs/codemirror/xquery.js";case"yaml":return cdn_url+"/3f7c/js/libs/codemirror/yaml.js";case"z80":return cdn_url+"/540d/js/libs/codemirror/z80.js";default:break}return null}var loading={};function splitCallback(cont,n){var count_down=n;return function(){count_down-=1;if(count_down==0)cont()}}function ensureDeps(mode,cont){var deps=CodeMirror.modes[mode].dependencies;var i;if(!deps)return cont();var missing=[];for(i=0;i<deps.length;i+=1){if(!CodeMirror.modes.hasOwnProperty(deps[i])){missing.push(deps[i])}}if(!missing.length)return cont();var split=splitCallback(cont,missing.length);for(i=0;i<missing.length;i+=1){CodeMirror.requireMode(missing[i],split)}}CodeMirror.requireMode=function(mode,cont){if(typeof mode!=="string")mode=mode.name;if(CodeMirror.modes.hasOwnProperty(mode))return ensureDeps(mode,cont);if(loading.hasOwnProperty(mode))return loading[mode].push(cont);var script=document.createElement("script");script.src=codemirrorMap(mode);var others=document.getElementsByTagName("script")[0];others.parentNode.insertBefore(script,others);loading[mode]=[cont];var list=loading[mode];var count=0;var poll=setInterval(function(){count+=1;if(count>100)return clearInterval(poll);if(CodeMirror.modes.hasOwnProperty(mode)){clearInterval(poll);loading[mode]=null;ensureDeps(mode,function(){for(var i=0;i<list.length;i+=1)list[i]()})}},200)};CodeMirror.autoLoadMode=function(instance,mode){if(!CodeMirror.modes.hasOwnProperty(mode)){CodeMirror.requireMode(mode,function(){instance.setOption("mode",instance.getOption("mode"))})}}})();

rem Move to the results directory so that the debugger files will go there.

cd ../results
grcompiler -D -c -w3531 awami_autogen.gdl "../source/AwamiNastaliqRegular.ttf" AwamiNastaliqRegular_gr.ttf
cd ../tools

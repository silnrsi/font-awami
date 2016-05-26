echo off
rem Needs to be run from the Awami root directory
echo on

perl c:/FontUtils/font-ttf-scripts/scripts/awami_makegdl -i "../source/nastaliq_rules.gdl" -a "source/Awami Nastaliq Regular_APs.xml" "source/Awami Nastaliq Regular.ttf" results/awami_autogen.gdl
copy results\awami_autogen.gdl source\autogen\awami_autogen.gdl

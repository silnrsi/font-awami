echo off
rem Needs to be run from the Awami root directory
echo on

perl c:/FontUtils/font-ttf-scripts/scripts/awami_makegdl -i "../source/nastaliq_rules.gdl" -a "source/AwamiNastaliqRegular_AP.xml" "source/AwamiNastaliqRegular.ttf" results/awami_autogen.gdl
copy results\awami_autogen.gdl source\autogen\awami_autogen.gdl

<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="html" encoding="utf-8"/>

<!--
This XSL stylesheet generates tables from a group of test strings, showing a waterfall at multiple sizes.
The top-level test group generates a section with a label and table.
Each test is shown in a row in the table, at four successive sizes.
The final cell in the row is the first test's comment.

The data should look something like:

<ftml>
  <head>
    <columns class="2%" comment="2%" label="10%" string="5%"/>
    <description>Page Title</description>
    <fontscale>100</fontscale>
    <fontsrc>local('Font Name'), url(filefile.ttf)</fontsrc>
    <title>Page Title</title>
    <styles><style feats=' ' name="default"/></styles>
  </head>
  <testgroup label="Group 1">
    <test label="word 1" rtl="True"><string>test string 1</string><comment>This is a comment.</comment></test>
    <test label="word 2" rtl="True"><string>test string 2</string></test>
    ...
-->

<!-- set variables from head element -->
<xsl:variable name="width-class" select="/ftml/head/columns/@class"/>
<xsl:variable name="width-comment" select="/ftml/head/columns/@comment"/>
<xsl:variable name="width-label" select="/ftml/head/columns/@label"/>
<xsl:variable name="width-string" select="/ftml/head/columns/@string"/>
<xsl:variable name="font-scale" select="concat(/ftml/head/fontscale, substring('100', 1 div not(/ftml/head/fontscale)))"/>

<!-- 
	Process the root node to construct the html page
-->
<xsl:template match="/">
<html>
	<head>
		<title>
			<xsl:value-of select="ftml/head/title"/>
		</title>
		<meta charset="utf-8"/>
		<meta name="description">
			<xsl:attribute name="content">
				<xsl:value-of select="ftml/head/description"/>
			</xsl:attribute>
		</meta>
		<style>
	body, td { font-family: sans-serif; }
	@font-face {font-family: TestFont; src: <xsl:value-of select="ftml/head/fontsrc"/>; }
	th { text-align: left; }
	table { width: 100%; table-layout: fixed; }
	table,th,td { padding: 20px; border: 1px solid #D8D8D8; border-collapse: collapse; }
<xsl:if test="$width-label != ''">
	.label { width: <xsl:value-of select="$width-label"/> }
</xsl:if>
<xsl:if test="$width-string != ''">
	.string {font-family: TestFont;}
</xsl:if>
<xsl:if test="$width-comment != ''">
	.comment {width: <xsl:value-of select="$width-comment"/>}
</xsl:if>
<xsl:if test="$width-class != ''">
	.comment {width: <xsl:value-of select="$width-class"/>}
</xsl:if>
	.dim {color: silver;}
	.bright {color: red;}
	<!-- NB: Uncomment the following to build separate css styles for each item in /ftml/head/styles -->
	<!-- <xsl:apply-templates select="/ftml/head/styles/*" /> -->
		</style>
	</head>
	
	<body>
		<h1><xsl:value-of select="/ftml/head/title"/></h1>
		<xsl:apply-templates select="/ftml/testgroup"/>
	</body>
</html>
</xsl:template>

<!-- 
	Build CSS style for FTML style element
-->
<xsl:template match="style">
	.<xsl:value-of select="@name"/> {
		font-family: TestFont; font-size: <xsl:value-of select="$font-scale"/>%;
<xsl:if test="@feats">
		-moz-font-feature-settings: <xsl:value-of select="@feats"/>;
		-ms-font-feature-settings: <xsl:value-of select="@feats"/>;
		-webkit-font-feature-settings: <xsl:value-of select="@feats"/>;
		font-feature-settings: <xsl:value-of select="@feats"/> ; 
</xsl:if>			
	}
</xsl:template>

<!-- 
	Process a testgroup, emitting a table containing all test records from the group
-->
<xsl:template match="testgroup">
	<h2><xsl:value-of select="@label"/></h2>
	<table>
		<tbody>
			<xsl:apply-templates/>
		</tbody>
	</table>
</xsl:template>

<!-- 
	Process a single test record, emitting a table row.
-->
<xsl:template match="test">
<tr>
	<xsl:if test="@background">
		<xsl:attribute name="style">background-color: <xsl:value-of select="@background"/>;</xsl:attribute>
	</xsl:if>
	<xsl:if test="$width-label != ''">
		<!-- emit label column -->
		<td class="label">
			<xsl:value-of select="@label"/>
		</td>
	</xsl:if>
	<xsl:if test="$width-string != ''">
		<!-- emit test data column -->
		<xsl:call-template name="cell">
			<xsl:with-param name="scale">1</xsl:with-param>
		</xsl:call-template>
		<xsl:call-template name="cell">
			<xsl:with-param name="scale">2</xsl:with-param>
		</xsl:call-template>
		<xsl:call-template name="cell">
			<xsl:with-param name="scale">5</xsl:with-param>
		</xsl:call-template>
		<xsl:call-template name="cell">
			<xsl:with-param name="scale">10</xsl:with-param>
		</xsl:call-template>
	</xsl:if>
	<xsl:if test="$width-comment != ''">
		<td class="comment">
			<!-- emit comment -->
			<xsl:value-of select="comment"/>
		</td>
	</xsl:if>
	<xsl:if test="$width-class != ''">
		<td class="class">
			<!-- emit class -->
			<xsl:value-of select="@class"/>
		</td>
	</xsl:if>
</tr>
</xsl:template>

<!-- 
	Emit html for one cell
-->
<xsl:template name="cell">
	<xsl:param name="scale">1</xsl:param> <!-- 1 = default -->
	
	<td class="string">   <!-- assume default string class -->
	<xsl:variable name="styleName" select="@class"/>
	<xsl:if test="$styleName != ''">
		<!-- emit lang attribute -->
		<xsl:apply-templates select="/ftml/head/styles/style[@name=$styleName]" mode="getLang"/>
	</xsl:if>
	<xsl:if test="@background">
		<xsl:attribute name="style">background-color: <xsl:value-of select="@background"/>;</xsl:attribute>
	</xsl:if>
	<xsl:if test="@rtl='True' ">
		<xsl:attribute name="dir">RTL</xsl:attribute>
	</xsl:if>
	<!-- emit style attribute with features and font-size -->
	<xsl:attribute name="style">
		<xsl:if test="$styleName != ''">
			<xsl:apply-templates select="/ftml/head/styles/style[@name=$styleName]" mode="getFeats"/>
		</xsl:if>
		font-size: <xsl:value-of select="$scale * $font-scale"/>%;
		width: 
		<xsl:choose>
			<xsl:when test="contains($width-label,'%')">
				<xsl:value-of select="$scale * substring-before($width-string,'%')"/>%;
			</xsl:when>
			<!-- would need other xsl:when elements to handle other suffixes: em, pt, etc. -->
			<xsl:otherwise> 
				<xsl:value-of select="$scale * $width-string"/>; 
			</xsl:otherwise>
		</xsl:choose>
	</xsl:attribute>
	
	<!-- and finally the test data -->
	<xsl:choose>
		<!-- if the test has an <em> marker, the use a special template -->
		<xsl:when test="string[em]">
			<xsl:apply-templates select="string" mode="hasEM"/>
		</xsl:when>
		<xsl:otherwise>
			<xsl:apply-templates select="string"/>
		</xsl:otherwise>
	</xsl:choose>
		</td>
</xsl:template>

<!-- 
	Emit html lang attribute.
-->
<xsl:template match="style" mode="getLang">
	<xsl:if test="@lang">
		<xsl:attribute name="lang">
			<xsl:value-of select="@lang"/>
		</xsl:attribute>
	</xsl:if>
</xsl:template>

<!-- 
	Emit html feature-settings (to add to style attribute).
-->
<xsl:template match="style" mode="getFeats">
	<xsl:if test="@feats">
-moz-font-feature-settings: <xsl:value-of select="@feats"/>;
-ms-font-feature-settings: <xsl:value-of select="@feats"/>;
-webkit-font-feature-settings: <xsl:value-of select="@feats"/>;
font-feature-settings: <xsl:value-of select="@feats"/>;
	</xsl:if>
</xsl:template>

<!--  
	Suppress all text nodes except those we really want.
-->
<xsl:template match="text()"/>

<!-- 
	for test strings that have no <em> children, emit text nodes without any adornment 
-->
<xsl:template match="string/text()">
	<xsl:value-of select="."/>
</xsl:template>

<!-- 
	for test strings that have <em> children, emit text nodes dimmed 
-->
<xsl:template match="string/text()" mode="hasEM">
	<span class="dim"><xsl:value-of select="."/></span>
</xsl:template>

<!-- 
	for <em> children of test strings, emit the text nodes with no adornment 
-->
<xsl:template match="em/text()" mode="hasEM">
	<!-- <span class="bright"><xsl:value-of select="."/></span> -->
	<xsl:value-of select="."/>
</xsl:template>

</xsl:stylesheet>


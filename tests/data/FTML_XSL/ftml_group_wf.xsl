<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="html" encoding="utf-8"/>

<!--
This XSL stylesheet generates waterfall tables with three sizes from a group of test strings.
The top-level test group generates a section with a label and table.
Each second-level testgroup is a single line of the of the table; the row label is taken from that
testgroup label.
The testgroup's test items are successive cells in the row, first at the smallest size, then the middle size,
and finally the largest size.
Any comments will be ignored.

The data should look something like:

<ftml>
  <head>
    <columns comment="15%" label="20%" string="15%"/>
    <description>Page Title</description>
    <fontscale>200</fontscale>
    <fontsrc>local('Font Name'), url(fontfile.ttf)</fontsrc>
    <title>Page Title</title>
    <styles><style feats=' ' name="default"/></styles>
  </head>
  <testgroup label="Section 1">
    <testgroup label="row 1" comment="comment 1">
      <test>
      	<comment>This is a comment - will be ignored</comment>
      	<string><em>test1</em></string>
      </test>
      <test><string>pre-context<em>test1</em></string></test>
      <test background="#cfcfcf"><string></string></test>
      <test background="#cfcfcf"><string></string></test>
    </testgroup>
    <testgroup label="row 2">
      <test><string><em>test2</em></string></test>
      <test><string>pre-context<em>test2</em></string></test>
      <test><string><em>test2</em>y</string>post-context</test>
      <test><string>pre-context<em>test2</em>post-context</string></test>
    </testgroup>
  </testgroup>
  ...
-->


<!-- set variables from head element -->
<xsl:variable name="width-class" select="/ftml/head/columns/@class"/>
<xsl:variable name="width-comment" select="/ftml/head/columns/@comment"/>
<xsl:variable name="width-label" select="/ftml/head/columns/@label"/>
<xsl:variable name="width-string" select="/ftml/head/columns/@string"/>
<xsl:variable name="font-scale" select="concat(/ftml/head/fontscale, substring('50', 1 div not(/ftml/head/fontscale)))"/>

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
		<!-- TOC anchor -->
		<a><xsl:attribute name="name">toc</xsl:attribute></a>
		
		<h1><xsl:value-of select="/ftml/head/title"/></h1>
		
		<!-- Generate table of contents -->
		<ul>
			<xsl:apply-templates select="/ftml/testgroup" mode="toc"/>
		</ul>
			
		<xsl:apply-templates select="/ftml/testgroup"/>
	</body>
</html>
</xsl:template>

<!-- 
	Build CSS style for FTML style element.
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
	Generate a table-of-contents link for the testgroup.
-->
<xsl:template match="ftml/testgroup" mode="toc">
	<li><a>
		<xsl:attribute name="href">#section<xsl:value-of select="position()"/></xsl:attribute>
		<xsl:value-of select="@label" />
	</a></li>
</xsl:template>


<!-- 
	Process a testgroup, emitting a table containing all test records from the group.
-->
<xsl:template match="testgroup">
	<!-- TOC anchor -->
	<a><xsl:attribute name="name">section<xsl:value-of select="position()"/></xsl:attribute></a>

	<h2><xsl:value-of select="@label"/></h2>
	<p><a><xsl:attribute name="href">#toc</xsl:attribute>[Table of Contents]</a></p>
	<table>
		<tbody>
			<xsl:apply-templates/> <!-- process second level testgroup -->
		</tbody>
	</table>
</xsl:template>

<!-- 
	Process a second level testgroup, emitting a table row.
-->
<xsl:template match="/ftml/testgroup/testgroup">
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

		<xsl:call-template name="oneSize">
			<xsl:with-param name="scale">1</xsl:with-param>
		</xsl:call-template>
		<xsl:call-template name="oneSize">
			<xsl:with-param name="scale">2</xsl:with-param>
		</xsl:call-template>
		<xsl:call-template name="oneSize">
			<xsl:with-param name="scale">4</xsl:with-param>
		</xsl:call-template>
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
	Generate a set of cells for a testgroup at a single size.
-->
<xsl:template name="oneSize">
	<xsl:param name="scale" />
	
	<xsl:apply-templates>
		<!-- Generate cells for each test at the given size. -->
		<xsl:with-param name="scale" select="$scale" />
	</xsl:apply-templates>

</xsl:template>


<!-- 
	Generate a cell for a test item at a single size.
-->
<xsl:template match="test">
	<xsl:param name="scale">1</xsl:param> <!-- 1 = default -->
	
	<td class="string">   <!-- assume default string class -->
	<xsl:variable name="styleName" select="@class"/>
	<xsl:if test="$styleName != ''">
		<!-- emit lang attribute -->
		<xsl:apply-templates select="/ftml/head/styles/style[@name=$styleName]" mode="getLang"/>
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
		<xsl:choose>
			<xsl:when test="contains($width-label,'%')">
				width: <xsl:value-of select="$scale * substring-before($width-string,'%')"/>%;
			</xsl:when>
			<!-- would need other xsl:when elements to handle other suffixes: em, pt, etc. -->
			<xsl:otherwise> 
				width: <xsl:value-of select="$scale * $width-string"/>; 
			</xsl:otherwise>
		</xsl:choose>
		<xsl:if test="@background">
			background-color: <xsl:value-of select="@background"/>;
		</xsl:if>
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
	For test strings that have no <em> children, emit text nodes without any adornment.
-->
<xsl:template match="string/text()">
	<xsl:value-of select="."/>
</xsl:template>

<!-- 
	For test strings that have <em> children, emit text nodes dimmed.
-->
<xsl:template match="string/text()" mode="hasEM">
	<span class="dim"><xsl:value-of select="."/></span>
</xsl:template>

<!-- 
	For <em> children of test strings, emit the text nodes with no adornment.
-->
<xsl:template match="em/text()" mode="hasEM">
	<!-- <span class="bright"><xsl:value-of select="."/></span> -->
	<xsl:value-of select="."/>
</xsl:template>

</xsl:stylesheet>


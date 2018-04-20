# Creates PDF test files.

#	This file is part of the Awami Nastaliq font 
#	(http://software.sil.org/awami) and is 
#	Copyright (c) 2014-2017 SIL International (http://www.sil.org/),
# with Reserved Font Names "Awami" and "SIL".
#
# This Font Software is licensed under the SIL Open Font License,
# Version 1.1.
#
#	You should have received a copy of the license along with this Font Software.
#	If this is not the case, go to (http://scripts.sil.org/OFL) for all the
#	details including an FAQ.


use Font::TTF::Font;
use Text::PDF::File;
use Text::PDF::Page;
use Text::PDF::TTFont0;
use Text::PDF::SFont;
use Text::PDF::Utils;
use JSON;
use Getopt::Long;

%opts = (size => 12, linespacing => 1.2, margins => 0.8, pagesize => 'a4', labelwidth => 0.5, labelsize => 9.5);
GetOptions(\%opts, 'font|f=s', 'output|o=s', 'size|s=i', 'linespacing|l=f', 'margins|m=f',
            'pagesize|p', 'labelwidth|w=f', 'labelsize|ls=f');

my %sizes = (
    'a4' => [595, 842],
    'ltr' => [612, 792]
);

my $pdf = Text::PDF::File->new;
$pdf->create_file($opts{'output'}) || die "Can't create pdf file $opts{'output'}";
$pdf->{' version'} = 3;
my $root = Text::PDF::Pages->new($pdf);
$root->proc_set('PDF', 'Text');
my ($maxx, $maxy) = @{$sizes{$opts{'pagesize'}}};
$root->bbox(0, 0, $maxx, $maxy);
my $font = Font::TTF::Font->open($opts{'font'}) || die "Can't open font file $opts{'font'} for reading";
my $tfont = Text::PDF::TTFont0->new($pdf, $font, "Ta0");
$root->add_font($tfont, $pdf);
$pdf_helv = Text::PDF::SFont->new($pdf, 'Helvetica', "FR");
$root->add_font($pdf_helv, $pdf);
my $t;
while(<>) { $t .= $_; }
my $json = decode_json($t);

my $page;
my ($curry, $page);
my ($upem) = $font->{'head'}{'unitsPerEm'};
my ($post) = $font->{'post'}->read;
my ($cmap) = $font->{'cmap'}->read;
my (@lines) = sort { $a <=> $b || $a cmp $b } keys %{$json};
foreach my $k (@lines)
{
    my ($v) = $json->{$k};
    unless (defined $page)
    {
        $page = Text::PDF::Page->new($pdf, $root);
        $curry = $maxy - $opts{'margins'} * 72 - $opts{'linespacing'} * $opts{'size'};
    }
    my ($currx) = ($opts{'margins'} + $opts{'labelwidth'}) * 72;
    my ($lwidth) = $pdf_helv->width($k) * 9.5 * 0.8;
    $page->add(sprintf("BT 1 0 0 1 %.2f %.2f Tm /FR %f Tf 80 Tz (%s) Tj ET\n", $currx - $lwidth - 3, $curry, $opts{'labelsize'}, $k));
    foreach my $glyph (@{$v->[0]})
    {
        next if ($glyph->[0] eq '_adv_');
        my ($gid) = $post->{'STRINGS'}{$glyph->[0]};
        if (!defined $gid)
        {
            if ($glyph->[0] =~ m/^glyph[0]*([0-9]+?)$/o)
            {
                $gid = $1;
            } elsif ($glyph->[0] =~ m/^uni([0-9A-Fa-f]+)$/o)
            {
                $gid = $cmap->ms_lookup(hex($1));
            } elsif ($glyph->[0] eq 'space')
            {
                $gid = 3;
            }
        }
        my ($x) = $glyph->[1] * $opts{'size'} / $upem + $currx;
        my ($y) = $glyph->[2] * $opts{'size'} / $upem + $curry;
        if ($x < $maxx)
        {
            $page->add(sprintf("BT 1 0 0 1 %.2f %.2f Tm /Ta0 %d Tf 100 Tz <%04X> Tj ET\n", $x, $y, $opts{'size'}, $gid));
        }
    }
    $curry -= $opts{'linespacing'} * $opts{'size'};
    if ($curry < $opts{'margins'} * 72)
    {
        $page->{' curstrm'}{'Filter'} = PDFArray(PDFName('FlateDecode'));
        $page->ship_out($pdf);
        $page = undef;
    }
}
if (defined $page)
{
    $page->{' curstrm'}{'Filter'} = PDFArray(PDFName('FlateDecode'));
    $page->ship_out($pdf);
}
$pdf->close_file;


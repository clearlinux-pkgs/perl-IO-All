#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-IO-All
Version  : 0.87
Release  : 28
URL      : https://cpan.metacpan.org/authors/id/F/FR/FREW/IO-All-0.87.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/F/FR/FREW/IO-All-0.87.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libi/libio-all-perl/libio-all-perl_0.87-1.debian.tar.xz
Summary  : 'IO::All to Larry Wall!'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-IO-All-license = %{version}-%{release}
Requires: perl-IO-All-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
IO::All - IO::All to Larry Wall!
VERSION
This document describes IO::All version 0.87.

%package dev
Summary: dev components for the perl-IO-All package.
Group: Development
Provides: perl-IO-All-devel = %{version}-%{release}
Requires: perl-IO-All = %{version}-%{release}

%description dev
dev components for the perl-IO-All package.


%package license
Summary: license components for the perl-IO-All package.
Group: Default

%description license
license components for the perl-IO-All package.


%package perl
Summary: perl components for the perl-IO-All package.
Group: Default
Requires: perl-IO-All = %{version}-%{release}

%description perl
perl components for the perl-IO-All package.


%prep
%setup -q -n IO-All-0.87
cd %{_builddir}
tar xf %{_sourcedir}/libio-all-perl_0.87-1.debian.tar.xz
cd %{_builddir}/IO-All-0.87
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/IO-All-0.87/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-IO-All
cp %{_builddir}/IO-All-0.87/LICENSE %{buildroot}/usr/share/package-licenses/perl-IO-All/fb79a8745bb44883b87def261357c3bbab912dc5
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-IO-All/9456935c7740ccc2ececdbd3ae4b42118a91753f
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/IO::All.3
/usr/share/man/man3/IO::All::DBM.3
/usr/share/man/man3/IO::All::Dir.3
/usr/share/man/man3/IO::All::File.3
/usr/share/man/man3/IO::All::Filesys.3
/usr/share/man/man3/IO::All::Link.3
/usr/share/man/man3/IO::All::MLDBM.3
/usr/share/man/man3/IO::All::Pipe.3
/usr/share/man/man3/IO::All::STDIO.3
/usr/share/man/man3/IO::All::Socket.3
/usr/share/man/man3/IO::All::String.3
/usr/share/man/man3/IO::All::Temp.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-IO-All/9456935c7740ccc2ececdbd3ae4b42118a91753f
/usr/share/package-licenses/perl-IO-All/fb79a8745bb44883b87def261357c3bbab912dc5

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-IO-All
Version  : 0.87
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/F/FR/FREW/IO-All-0.87.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/F/FR/FREW/IO-All-0.87.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libi/libio-all-perl/libio-all-perl_0.87-1.debian.tar.xz
Summary  : 'IO::All to Larry Wall!'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-IO-All-license = %{version}-%{release}
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

%description dev
dev components for the perl-IO-All package.


%package license
Summary: license components for the perl-IO-All package.
Group: Default

%description license
license components for the perl-IO-All package.


%prep
%setup -q -n IO-All-0.87
cd ..
%setup -q -T -D -n IO-All-0.87 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/IO-All-0.87/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-IO-All
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-IO-All/LICENSE
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
/usr/lib/perl5/vendor_perl/5.26.1/IO/All.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/All.pod
/usr/lib/perl5/vendor_perl/5.26.1/IO/All/Base.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/All/DBM.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/All/DBM.pod
/usr/lib/perl5/vendor_perl/5.26.1/IO/All/Dir.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/All/Dir.pod
/usr/lib/perl5/vendor_perl/5.26.1/IO/All/File.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/All/File.pod
/usr/lib/perl5/vendor_perl/5.26.1/IO/All/Filesys.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/All/Filesys.pod
/usr/lib/perl5/vendor_perl/5.26.1/IO/All/Link.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/All/Link.pod
/usr/lib/perl5/vendor_perl/5.26.1/IO/All/MLDBM.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/All/MLDBM.pod
/usr/lib/perl5/vendor_perl/5.26.1/IO/All/Pipe.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/All/Pipe.pod
/usr/lib/perl5/vendor_perl/5.26.1/IO/All/STDIO.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/All/STDIO.pod
/usr/lib/perl5/vendor_perl/5.26.1/IO/All/Socket.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/All/Socket.pod
/usr/lib/perl5/vendor_perl/5.26.1/IO/All/String.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/All/String.pod
/usr/lib/perl5/vendor_perl/5.26.1/IO/All/Temp.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/All/Temp.pod

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
/usr/share/package-licenses/perl-IO-All/LICENSE

# symlookup spec file
# Copyright © 2007-2010 Andrew Savchenko
#
# This file is part of symlookup.
#
# symlookup is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation
#
# symlookup is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License version 3 for more details.
#
# You should have received a copy of the GNU General Public License version 3
# along with symlookup. If not, see <http://www.gnu.org/licenses/>.
#

Name: symlookup
Version: 0.3.5
Release: 1
Source:  %name-%version.tar.bz2
Summary: Object symbol search utility
License: GPL
URL: https://symbol-lookup.sourceforge.net
Group: System/Utilities
Prefix: %_prefix
BuildRoot: %_tmppath/%name
Obsoletes: symbol_lookup
Requires: elfutils-libelf rpm-libs
BuildRequires: elfutils-libelf-devel rpm-devel

%description
symlookup is an utility intended for object symbols search in
dynamic or static symbol libraries. It looks up for libraries where
given symbols are defined and optionally can find rpms provided these
libraries.

%prep
%setup -q -n %name

%build
%configure --disable-strip
make %?_smp_mflags

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%files
%defattr(-,root,root)
%_docdir/*
%_bindir/*
%_mandir/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Apr 25 2010 Savchenko Andrew <bircoph@users.sourceforge.net>
- updated for v0.3.2

* Wed Jun 27 2007 Savchenko Andrew <bircoph@users.sourceforge.net>
- initial RPM

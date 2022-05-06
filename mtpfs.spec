Summary:	MTPfs - FUSE filesystem that supports reading and writing from any MTP device
Summary(pl.UTF-8):	MTPfs - system plików FUSE obsługujący odczyt i zapis na urządzenia MTP
Name:		mtpfs
Version:	1.1
Release:	1
License:	GPL v3
Group:		Applications/System
Source0:	https://www.adebenham.com/files/mtp/%{name}-%{version}.tar.gz
# Source0-md5:	a299cadca336e6945b7275b44c6e8d27
URL:		https://www.adebenham.com/mtpfs/
BuildRequires:	glib2-devel >= 1:2.30
BuildRequires:	libfuse-devel >= 2.2
BuildRequires:	libid3tag-devel >= 0.15
BuildRequires:	libmad-devel >= 0.15
BuildRequires:	libmtp-devel >= 1.1.2
BuildRequires:	pkgconfig
Requires:	glib2 >= 1:2.30
Requires:	libfuse-tools >= 2.2
Requires:	libid3tag >= 0.15
Requires:	libmad >= 0.15
Requires:	libmtp >= 1.1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MTPfs is a FUSE filesystem that supports reading and writing from any
MTP device (as supported by libmtp).

Currently implemented:
- Support multiple storage areas
- Browsing Folders
- Reading files
- Writing files
- Browsing playlists
- Writing playlists
- Writing music tracks with metadata

%description -l pl.UTF-8
MTPfs to system plików FUSE obsługujący odczyt i zapis na dowolne
urządzenia MTP (obsługiwane przez libmtp).

Obecnie zaimplementowane:
- przeglądanie wielu obszarów przechowywania danych
- przeglądanie folderów
- odczyt plików
- zapis plików
- przeglądanie list odtwarzania
- zapis list odtwarzania
- zapis ścieżek muzycznych z metadanymi

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/mtpfs

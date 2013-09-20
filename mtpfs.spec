Summary:	MTPfs is a FUSE filesystem that supports reading and writing from any MTP device
Name:		mtpfs
Version:	1.1
Release:	1
License:	GPL v3
Group:		Applications/System
Source0:	http://www.adebenham.com/files/mtp/%{name}-%{version}.tar.gz
# Source0-md5:	a299cadca336e6945b7275b44c6e8d27
URL:		http://www.adebenham.com/mtpfs/
BuildRequires:	pkgconfig
BuildRequires:	libfuse-devel
BuildRequires:	libmtp-devel
BuildRequires:	glib2-devel
BuildRequires:	libmad-devel
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

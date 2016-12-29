Summary: NethServer diagnostic tools
%define name nethserver-diagtools
%define version 0.0.1
%define release 1
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: http://dev.nethserver.org/projects/nethforge/wiki/%{name}
BuildRequires: nethserver-devtools
#AutoReq: no

%description
NethServer diagnostic tool
%prep
%setup

%post
%preun

%build
%{makedocs}
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)

%{genfilelist} %{buildroot} \
  --file /usr/libexec/nethserver/ipAddr 'attr(0755,root,root)' \
  --file /usr/libexec/nethserver/ipRoute 'attr(0755,root,root)' \
  --file /usr/libexec/nethserver/pingHost 'attr(0755,root,root)' \
  --file /usr/libexec/nethserver/nsLookup 'attr(0755,root,root)' \
  --file /usr/libexec/nethserver/traceRoute 'attr(0755,root,root)' \
$RPM_BUILD_ROOT > e-smith-%{version}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f e-smith-%{version}-filelist
%defattr(-,root,root)

%dir %{_nseventsdir}/%{name}-update

%changelog
* Wed Nov 23 2016 Stephane de Labrusse <stephdl@de-labrusse.fr> - 0.0.1-1-ns7
- First release
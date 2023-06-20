Summary: Install all LINSTOR dependencies
Name: xcp-ng-linstor
Version: 1.1
Release: 2%{?dist}
License: GPLv2
Source0: 99-enable-sm-driver-linstor.conf
BuildArch: noarch

Requires: drbd
Requires: drbd-reactor
Requires: http-nbd-transfer
Requires: kmod-drbd
Requires: linstor-client
Requires: linstor-controller
Requires: linstor-satellite

# To remove after stable release of LINSTOR.
Requires: blktap-linstor
Requires: sm-linstor

%description
Install all LINSTOR dependencies from LINSTOR XCP-ng repository.

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/xapi.conf.d/99-enable-sm-driver-linstor.conf

%files
%{_sysconfdir}/xapi.conf.d/99-enable-sm-driver-linstor.conf

%changelog
* Tue Jun 20 2023 Ronan Abhamon <ronan.abhamon@vates.fr> - 1.1-2
- Add Requires to install specific versions of blktap and sm.

* Tue May 30 2023 Ronan Abhamon <ronan.abhamon@vates.fr> - 1.1-1
- Add 99-enable-sm-driver-linstor.conf.

* Mon Mar 13 2023 Ronan Abhamon <ronan.abhamon@vates.fr> - 1.0-1
- Add new drbd-reactor dependency that replaces minidrbdcluster.

* Tue May 24 2022 Ronan Abhamon <ronan.abhamon@vates.fr> - 0.9.0-1
- Initial release.

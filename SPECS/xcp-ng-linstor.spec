Summary: Install all LINSTOR dependencies
Name: xcp-ng-linstor
Version: 0.9.0
Release: 1%{?dist}
License: GPLv2
BuildArch: noarch

Requires: drbd
Requires: http-nbd-transfer
Requires: kmod-drbd
Requires: linstor-client
Requires: linstor-controller
Requires: linstor-satellite

%description
Install all LINSTOR dependencies from LINSTOR XCP-ng repository.

%files

%changelog
* Tue May 24 2022 Ronan Abhamon <ronan.abhamon@vates.fr> - 0.9.0-1
- Initial release.

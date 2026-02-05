Summary: Install all LINSTOR dependencies
Name: xcp-ng-linstor
Version: 1.2
Release: 6%{?dist}
License: GPLv2
Source0: 99-enable-sm-driver-linstor.conf
BuildArch: noarch

Requires: drbd
Requires: drbd-reactor
Requires: http-nbd-transfer
Requires: kmod-drbd
Requires: linstor-client
Requires: linstor-controller >= 1.33.1
Requires: linstor-satellite >= 1.33.1

%description
Install all LINSTOR dependencies from LINSTOR XCP-ng repository.

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/xapi.conf.d/99-enable-sm-driver-linstor.conf

%files
%{_sysconfdir}/xapi.conf.d/99-enable-sm-driver-linstor.conf

%triggerin -- drbd-reactor
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%changelog
* Fri Feb 06 2026 Ronan Abhamon <ronan.abhamon@vates.tech> - 1.2-6
- Update controller/satellite requires to 1.33.1.

* Fri Jan 23 2026 Damien Thenot <damien.thenot@vates.tech> - 1.2-5
- Add trigger to reload systemd units for drbd-reactor

* Wed Dec 10 2025 Ronan Abhamon <ronan.abhamon@vates.tech> - 1.2-4
- Update controller/satellite requires to 1.33.0~rc.2-1.

* Fri Oct 31 2025 Damien Thenot <damien.thenot@vates.tech> - 1.2-3
- Add version requirements

* Mon Sep 16 2024 Damien Thenot <damien.thenot@vates.tech> - 1.2-2
- Add largeblock to 99-enable-sm-driver-linstor.conf.

* Wed Jun 28 2023 Ronan Abhamon <ronan.abhamon@vates.fr> - 1.2-1
- Build for XCP-ng 8.3.
- Remove blktap and sm requirements.

* Tue Jun 20 2023 Ronan Abhamon <ronan.abhamon@vates.fr> - 1.1-2
- Add Requires to install specific versions of blktap and sm.

* Tue May 30 2023 Ronan Abhamon <ronan.abhamon@vates.fr> - 1.1-1
- Add 99-enable-sm-driver-linstor.conf.

* Mon Mar 13 2023 Ronan Abhamon <ronan.abhamon@vates.fr> - 1.0-1
- Add new drbd-reactor dependency that replaces minidrbdcluster.

* Tue May 24 2022 Ronan Abhamon <ronan.abhamon@vates.fr> - 0.9.0-1
- Initial release.

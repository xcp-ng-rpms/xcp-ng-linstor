Summary: Install all LINSTOR dependencies
Name: xcp-ng-linstor
Version: 1.2
Release: 8%{?dist}
License: GPLv2
Source0: 99-enable-sm-driver-linstor.conf
Source1: xcp-ng-linstor.conf
Source2: xcp-ng-linstor-java-env.conf
BuildArch: noarch

BuildRequires: systemd

Requires: drbd
Requires: drbd-reactor
Requires: http-nbd-transfer
Requires: kmod-drbd
Requires: linstor-client
Requires: linstor-controller >= 1.35.3
Requires: linstor-satellite >= 1.35.3
Requires: systemd

%description
Install all LINSTOR dependencies from LINSTOR XCP-ng repository.

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/xapi.conf.d/99-enable-sm-driver-linstor.conf
install -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/xapi-domains.service.d/xcp-ng-linstor.conf
install -D -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/linstor-controller.service.d/xcp-ng-linstor-java-env.conf
install -D -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/linstor-satellite.service.d/xcp-ng-linstor-java-env.conf

%files
%{_sysconfdir}/xapi.conf.d/99-enable-sm-driver-linstor.conf
%dir %{_unitdir}/xapi-domains.service.d
%{_unitdir}/xapi-domains.service.d/xcp-ng-linstor.conf
%dir %{_unitdir}/linstor-controller.service.d
%dir %{_unitdir}/linstor-satellite.service.d
%{_unitdir}/linstor-controller.service.d/xcp-ng-linstor-java-env.conf
%{_unitdir}/linstor-satellite.service.d/xcp-ng-linstor-java-env.conf

%post
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%triggerin -- drbd-reactor linstor-controller linstor-satellite
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%changelog
* Mon Oct 26 2026 Alexandre Sollier <alexandre.sollier@vates.tech> - 1.2-8
- Update controller/satellite requires to 1.35.3.
- Set the `JAVA_HOME` environment variable on the controller/satellite services for XCP-ng's Java 21 distribution.

* Fri Oct 09 2026 Gaëtan Lehmann <gaetan.lehmann@vates.tech> - 1.2-7
- Ensure LINSTOR services shut down after xapi-domains.

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

Summary:	KRunner integration for KDE Telepathy contacts
Name:		ktp-contact-runner
Version:	21.12.2
Release:	1
Epoch:		1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Designer)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	cmake(Qt5Script)
BuildRequires:	cmake(Qt5ScriptTools)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5WebKit)
BuildRequires:	cmake(Qt5TextToSpeech)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5Runner)
BuildRequires:	cmake(KTp)
BuildRequires:	cmake(TelepathyLoggerQt)

%description
KRunner integration for KDE Telepathy contacts

%files -f plasma_runner_ktp_contacts.lang
%{_libdir}/qt5/plugins/kf5/krunner/krunner_ktp_contacts.so

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang plasma_runner_ktp_contacts

Name:       harbour-sailmines

Summary:    Minesweeper clone for SFOS
Version:    0.9
Release:    1
License:    MIT
URL:        https://github.com/sharks-dev/harbour-sailmines
Source0:    %{name}-%{version}.tar.bz2
Requires:   sailfishsilica-qt5 >= 0.10.9
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  desktop-file-utils
Obsoletes: SailMines

%description
Minesweeper clone for SFOS

# This description section includes metadata for SailfishOS:Chum, see
# https://github.com/sailfishos-chum/main/blob/main/Metadata.md
%if 0%{?_chum}
Title: Sailmines
Type: desktop-application
DeveloperName: Sharks
PackagedBy: Sharks
Categories:
 - Game
Custom:
  Repo: https://github.com/sharks-dev/harbour-sailmines
PackageIcon: https://github.com/sharks-dev/harbour-sailmines/raw/main/icons/172x172/harbour-sailmines.png
Screenshots:
 - https://github.com/sharks-dev/harbour-sailmines/raw/main/screenshots/won.png
 - https://github.com/sharks-dev/harbour-sailmines/raw/main/screenshots/lost.png
 - https://github.com/sharks-dev/harbour-sailmines/raw/main/screenshots/zoomOut.png
 - https://github.com/sharks-dev/harbour-sailmines/raw/main/screenshots/settings.png
Links:
  Homepage: https://github.com/sharks-dev/harbour-sailmines
  Bugtracker: https://github.com/sharks-dev/harbour-sailmines/issues
%endif

%prep
%setup -q -n %{name}-%{version}

%build

%qmake5 

%make_build


%install
%qmake5_install


desktop-file-install --delete-original         --dir %{buildroot}%{_datadir}/applications                %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

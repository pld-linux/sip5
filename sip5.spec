Summary:	SIP - Python/C++ Bindings Generator
Summary(pl.UTF-8):	SIP - generator wiązań Python/C++
Name:		sip5
Version:	5.5.0
Release:	5
License:	GPL v2
#Source0Download: https://pypi.org/simple/sip/
Source0:	https://files.pythonhosted.org/packages/source/s/sip/sip-%{version}.tar.gz
# Source0-md5:	657c52aff0a180fc0f481e210bc9a2ba
Patch0:		python3.10.patch
URL:		https://www.riverbankcomputing.com/software/sip
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-setuptools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SIP is a collection of tools that makes it very easy to create Python
bindings for C and C++ libraries. It was originally developed in 1998
to create PyQt, the Python bindings for the Qt toolkit, but can be
used to create bindings for any C or C++ library. For example it is
also used to generate wxPython, the Python bindings for wxWidgets.

%description -l pl.UTF-8
SIP to zbiór narzędzi ułatwiających tworzenie wiązań Pythona do
bibliotek C i C++. Pierwotnie powstał w 1998 roku, aby stworzyć PyQt -
wiązań Pythona do biblioteki Qt, ale może być używany do tworzenia
wiązań do dowolnej biblioteki C lub C++. Jest używana także np. do
generowania wxPythona - wiązań Pythona do wxWidgets.

%prep
%setup -q -n sip-%{version}
%patch0 -p1

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/sip-build
%attr(755,root,root) %{_bindir}/sip-distinfo
%attr(755,root,root) %{_bindir}/sip-install
%attr(755,root,root) %{_bindir}/sip-module
%attr(755,root,root) %{_bindir}/sip-sdist
%attr(755,root,root) %{_bindir}/sip-wheel
%attr(755,root,root) %{_bindir}/sip5
%{py3_sitedir}/sip-%{version}-py*.egg-info
%dir %{py3_sitedir}/sipbuild
%{py3_sitedir}/sipbuild/*.py
%attr(755,root,root) %{py3_sitedir}/sipbuild/*.so
%{py3_sitedir}/sipbuild/__pycache__
%dir %{py3_sitedir}/sipbuild/distinfo
%{py3_sitedir}/sipbuild/distinfo/*.py
%{py3_sitedir}/sipbuild/distinfo/__pycache__
%dir %{py3_sitedir}/sipbuild/legacy
%{py3_sitedir}/sipbuild/legacy/*.py
%{py3_sitedir}/sipbuild/legacy/__pycache__
%dir %{py3_sitedir}/sipbuild/module
%{py3_sitedir}/sipbuild/module/*.py
%{py3_sitedir}/sipbuild/module/__pycache__
%{py3_sitedir}/sipbuild/module/source
%dir %{py3_sitedir}/sipbuild/tools
%{py3_sitedir}/sipbuild/tools/*.py
%{py3_sitedir}/sipbuild/tools/__pycache__

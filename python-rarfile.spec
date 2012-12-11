%define	module	rarfile
%define name	python-%{module}
%define version 2.5
%define	rel	1
%if %mdkversion	< 201100
%define release %mkrel %{rel}
%else
%define	release	%{rel}
%endif

Summary:	RAR archive reader for Python
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/r/%{module}/%{module}-%{version}.tar.gz
License:	ISC
Group:		Development/Python
Url:		https://github.com/markokr/rarfile/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	unrar

%description
This is a Python module for RAR archive reading. The interface is
similar to that of the zipfile module.

%prep
%setup -q -n %{module}-%{version}

%build
%__python setup.py build 

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc FAQ LICENSE NEWS README
%py_sitedir/%{module}*


%changelog
* Wed Sep 05 2012 Lev Givon <lev@mandriva.org> 2.5-1
+ Revision: 816360
- imported package python-rarfile


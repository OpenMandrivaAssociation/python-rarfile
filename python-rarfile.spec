%define	module	rarfile

Summary:	RAR archive reader for Python
Name:		python-%{module}
Version:	2.6
Release:	2
Source0:	https://pypi.python.org/packages/source/r/rarfile/rarfile-%{version}.tar.gz
License:	ISC
Group:		Development/Python
Url:		https://github.com/markokr/rarfile/
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
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean

%files
%doc  LICENSE  
%py_puresitedir/%{module}*

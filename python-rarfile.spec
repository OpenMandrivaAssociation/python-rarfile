%define	module	rarfile

Summary:	RAR archive reader for Python
Name:		python-%{module}
Version:	4.0
Release:	1
Source0:	https://pypi.python.org/packages/source/r/rarfile/rarfile-%{version}.tar.gz
License:	ISC
Group:		Development/Python
Url:		https://github.com/markokr/rarfile/
BuildArch:	noarch
BuildRequires:	python-setuptools
Requires:	unrar

%description
This is a Python module for RAR archive reading. The interface is
similar to that of the zipfile module.

%prep
%setup -q -n %{module}-%{version}

%build
%__python setup.py build 

%install
PYTHONDONTWRITEBYTECODE=1 %__python setup.py install --root=%{buildroot}

%clean

%files
%doc  LICENSE  
%py_puresitedir/%{module}*

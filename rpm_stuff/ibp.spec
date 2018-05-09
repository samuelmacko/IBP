Name:           ibp
Version:        0.1.1
Release:        1%{?dist}
Summary:        aaaaaaaaa

License:        GPLv3+
URL:            https://example.com/%{name}
Source0:        https://example.com/%{name}/release/%{name}-%{version}.tar.gz

BuildRequires:  python3
Requires:       python3
Requires:	python3-qt5
Requires:	python3-ovirt-engine-sdk4

BuildArch:      noarch

%description
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

%prep
%setup -q

%build

python3 -m compileall .

%install

mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/usr/lib/%{name}

cat > %{buildroot}/%{_bindir}/%{name} <<-EOF
#!/bin/bash
/usr/bin/python3 /usr/lib/%{name}/main.pyc
EOF

chmod 0755 %{buildroot}/%{_bindir}/%{name}

install -m 0644 main.py* %{buildroot}/usr/lib/%{name}/

%files
%license LICENSE
%dir /usr/lib/%{name}/
%{_bindir}/%{name}
/usr/lib/%{name}/main.py*

%changelog
* Mon May  7 2018 Samuel Macko <smacko@redhat.com>
  - First try

# Generated from cucumber-gherkin-21.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name cucumber-gherkin

Name: rubygem-%{gem_name}
Version: 21.0.0
Release: 1%{?dist}
Summary: cucumber-gherkin-21.0.0
License: MIT
URL: https://github.com/cucumber/gherkin-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.3
# BuildRequires: rubygem(rspec) >= 3.10
# BuildRequires: rubygem(rspec) < 4
# BuildRequires: rubygem(rspec) >= 3.10.0
BuildArch: noarch

%description
Gherkin parser.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
# rspec spec
popd

%files
%dir %{gem_instdir}
%{_bindir}/gherkin-ruby
%{_bindir}/gherkin
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/spec

%changelog
* Wed Sep 08 2021 Jarek Prokop <jprokop@redhat.com> - 21.0.0-1
- Initial package

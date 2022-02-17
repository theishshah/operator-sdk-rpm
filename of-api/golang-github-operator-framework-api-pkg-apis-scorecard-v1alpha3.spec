# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/operator-framework/api
%global goipath         github.com/operator-framework/api
Version:                0.13.0

%gometa

%global common_description %{expand:
Contains the API definitions used by OLM and Marketplace.}

%global golicenses      LICENSE
%global godocs          README.md RELEASE.md hack/boilerplate.go.txt

Name:           %{goname}
Release:        1%{?dist}
Summary:        Contains the API definitions used by OLM and Marketplace

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/schema)
BuildRequires:  golang(github.com/blang/semver)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(k8s.io/api/admissionregistration/v1)
BuildRequires:  golang(k8s.io/api/apps/v1)
BuildRequires:  golang(k8s.io/api/core/v1)
BuildRequires:  golang(k8s.io/api/policy/v1beta1)
BuildRequires:  golang(k8s.io/api/rbac/v1)
BuildRequires:  golang(k8s.io/api/scheduling/v1)
BuildRequires:  golang(k8s.io/apiextensions-apiserver/pkg/apis/apiextensions)
BuildRequires:  golang(k8s.io/client-go/tools/record)
BuildRequires:  golang(sigs.k8s.io/controller-runtime/pkg/scheme)
BuildRequires:  golang(k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/validation)
BuildRequires:  golang(k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1beta1)
BuildRequires:  golang(k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
pwd
ls
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc README.md RELEASE.md hack/boilerplate.go.txt
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Feb 15 2022 Ish Shah <ishah@redhat.com> - 0.13.0-1%{?dist}
- Initial package

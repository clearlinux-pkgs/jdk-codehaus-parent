Name     : jdk-codehaus-parent
Version  : 4
Release  : 2
URL      : http://repo1.maven.org/maven2/org/codehaus/codehaus-parent/4/codehaus-parent-4.pom
Source0  : http://repo1.maven.org/maven2/org/codehaus/codehaus-parent/4/codehaus-parent-4.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : apache-maven
BuildRequires : apache-maven2
BuildRequires : javapackages-tools
BuildRequires : jdk-aether
BuildRequires : jdk-aopalliance
BuildRequires : jdk-apache-parent
BuildRequires : jdk-atinject
BuildRequires : jdk-bsh
BuildRequires : jdk-cdi-api
BuildRequires : jdk-commons-cli
BuildRequires : jdk-commons-codec
BuildRequires : jdk-commons-collections
BuildRequires : jdk-commons-compress
BuildRequires : jdk-commons-io
BuildRequires : jdk-commons-lang
BuildRequires : jdk-commons-lang3
BuildRequires : jdk-commons-logging
BuildRequires : jdk-commons-parent
BuildRequires : jdk-doxia
BuildRequires : jdk-doxia-sitetools
BuildRequires : jdk-enforcer
BuildRequires : jdk-guava
BuildRequires : jdk-guice
BuildRequires : jdk-httpcomponents-client
BuildRequires : jdk-httpcomponents-core
BuildRequires : jdk-jsoup
BuildRequires : jdk-jsr-305
BuildRequires : jdk-log4j
BuildRequires : jdk-maven-archiver
BuildRequires : jdk-maven-common-artifact-filters
BuildRequires : jdk-maven-dependency-tree
BuildRequires : jdk-maven-invoker
BuildRequires : jdk-maven-javadoc-plugin
BuildRequires : jdk-maven-plugin-testing
BuildRequires : jdk-maven-plugin-tools
BuildRequires : jdk-maven-reporting-api
BuildRequires : jdk-maven-shared-utils
BuildRequires : jdk-objectweb-asm
BuildRequires : jdk-plexus-archiver
BuildRequires : jdk-plexus-cipher
BuildRequires : jdk-plexus-classworlds
BuildRequires : jdk-plexus-containers
BuildRequires : jdk-plexus-i18n
BuildRequires : jdk-plexus-interactivity
BuildRequires : jdk-plexus-interpolation
BuildRequires : jdk-plexus-io
BuildRequires : jdk-plexus-sec-dispatcher
BuildRequires : jdk-plexus-utils
BuildRequires : jdk-plexus-velocity
BuildRequires : jdk-sisu
BuildRequires : jdk-slf4j
BuildRequires : jdk-snappy
BuildRequires : jdk-snappy-java
BuildRequires : jdk-velocity
BuildRequires : jdk-wagon
BuildRequires : jdk-xbean
BuildRequires : jdk-xmlunit
BuildRequires : jdk-xz
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six
BuildRequires : xmvn

%description
No detailed description available

%prep
mv %{SOURCE0} pom.xml

%build
python3 /usr/share/java-utils/mvn_build.py

%install
xmvn-install  -R .xmvn-reactor -n codehaus-parent -d %{buildroot}

%files
%defattr(-,root,root,-)
/usr/share/maven-metadata/codehaus-parent.xml
/usr/share/maven-poms/codehaus-parent/codehaus-parent.pom

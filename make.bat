@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

set ACTION=%1
set PRODUCT=%2
set LANGUAGE=%3

if "%LANGUAGE%" == "" (
	set LANGUAGE=en
)

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=python -msphinx
)
set SOURCEDIR=source

set BUILDDIR=build
if NOT "%ACTION%" == "gettext" (
    set BUILDDIR=%BUILDDIR%\%LANGUAGE%
)

if "%1" == "" goto help

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The Sphinx module was not found. Make sure you have Sphinx installed,
	echo.then set the SPHINXBUILD environment variable to point to the full
	echo.path of the 'sphinx-build' executable. Alternatively you may add the
	echo.Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.http://sphinx-doc.org/
	exit /b 1
)

%SPHINXBUILD% -M %ACTION% %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% -Dlanguage=%LANGUAGE% -t%PRODUCT%
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS%

:end
popd

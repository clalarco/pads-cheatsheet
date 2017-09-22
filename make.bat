@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

set PRODUCT=%1
set LANGUAGE=%2

if %LANGUAGE% == "" (
	set LANGAUGE=en
)

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=python -msphinx
)
set SOURCEDIR=.
set BUILDDIR=_build\%LANGUAGE%

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

%SPHINXBUILD% -M singlehtml %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% -Dlanguage=%LANGUAGE% -t%PRODUCT%
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS%

:end
popd

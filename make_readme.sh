#!/usr/bin/env bash
##############################################################################
# Genera la documentacion de los modulos, requiere la instalacion de oca
# maintainers tools
# https://github.com/OCA/maintainer-tools
#
source /opt/maintainer-tools/env/bin/activate
oca-gen-addon-readme \
	--org-name jobiols \
	--repo-name cl-amic \
	--branch 11.0 \
	--addons-dir "$PWD" \
	--gen-html

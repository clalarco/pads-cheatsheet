.. include:: /common/icons-logos.rst

========================================
Rules
========================================

Open Dialog
----------------------------------------
Setup > Design Rules... and select scope:

.. note::
    **Scopes**
    - **Default** Set rules for all nets
    - **Net** Set rules per net, overriding Default

.. hint::
    - **"Report"** generates a report with rules

.. note::
    **Sections**
    - **Clearance** Set trace widths and separations
    - **Routing** Set layers to route and via types


Set Trace Width
----------------------------------------
Clearance > Trace width

Set separation for different nets
----------------------------------------
Clearance > Clerance section

Set separation of objects for same net
----------------------------------------
Clearance > Same net Section

Allow Via at SMD
----------------------------------------
Clearance > Same net > Via/SMD set 0

Components separation
----------------------------------------
Clearance > Other > Body to Body

Drills separation
----------------------------------------
Clearance > Other > Drill to drill

Set allowed Layers
----------------------------------------
Routing > Layer biasing (selected = enabled)

Set allowed via types
----------------------------------------
Routing > Vias (selected = enabled)

Set maximum number of vias
----------------------------------------
Routing > maximum number of vias

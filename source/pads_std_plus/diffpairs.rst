.. include:: /common/icons-logos.rst

****************************************
Diff Pairs
****************************************

.. container:: side-images

    .. figure:: _static/img/d-diffpair-separation.png

        Separation and Spacing

    .. figure:: _static/img/d-diffpair-via-type.png

        Via types


========================================
Setup
========================================

Set Diff Pair in schematics
----------------------------------------
#. Select net
#. In Properties, set the pair net in 'diff pair' field

Set diff pair in constraint manager:
----------------------------------------
#. |i-constraint-manager|
#. Edit > Differential Pairs > Auto Assign Differential Pairs...
#. Set patterns for Net name and Pair net Name
#. Click Apply

   .. hint:: Nets set in schematics won't appear in auto assign dialog

Set Diff Pair Spacing
----------------------------------------
#. At Net Classes select class
#. Change Differential Spacing

Set Max Separation
----------------------------------------
#. At Constraint Classes select the class
#. Select 'Nets' tab
#. Select class or net
#. Set Separation Distance

Set diff pair length
----------------------------------------
In constraint manager (|i-constraint-manager|)

#. Click in constraint classes
#. Select diffpair
#. Set Min and max length.

========================================
Routing
========================================

Route Diff pairs
----------------------------------------

In Router (|i-pads-router|) Same as route a single trace

Change leader routing trace
----------------------------------------
``tab``

Split traces
----------------------------------------
``Ctrl+X``

Route separately/join
----------------------------------------
``Ctrl+Z``

Set via pattern
----------------------------------------
While routing:

#. ``RClick`` > Via Pattern
#. Select via type

Tune diff pairs
----------------------------------------
#. In router (|i-pads-router|)
#. ``RClick`` > Select nets
#. Click on one net of diff pair
#. ``RClick`` > Select Differential pairs
#. ``RClick`` > Tune

Tune diff pair Options
----------------------------------------
In Router (|i-pads-router|) Tools > Options > Routing Page > Tune

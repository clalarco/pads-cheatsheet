.. include:: /common/icons-logos.rst

========================================
Routing
========================================

Setup Dynamic Route and Bus Route
----------------------------------------
#. Tools > Options > Design
#. Set On-line DRC to Prevent

Begin
----------------------------------------

.. only:: not pads_maker

    #. |i-pads-router|


#. ``RClick`` > Select Pins/Traces/Unroutes

Start route
----------------------------------------
#. ``LClick`` over pin or trace
#. ``F3``

Confirm a segment
----------------------------------------
``LClick`` or ``space``

Undo a segment
----------------------------------------
``Backspace``

Change Layer
----------------------------------------
``F4`` or ``l<n>``

Autocomplete
----------------------------------------
``Double LClick``

Stop Routing
----------------------------------------
``Ctrl+LClick``

Change Width
----------------------------------------
``w<width>``

Add a via
----------------------------------------
``Shift+LClick``

Add testpoint
----------------------------------------
While routing ``RClick`` > Add testpoint

Add jumper
----------------------------------------

1. While routing ``RClick`` > Add jumper
2. Select orentation and length


Via at SMD
----------------------------------------

.. only:: pads_std_plus

    In Layout (|i-pads-layout|)

#. ``RClick`` > Select Traces/Pins
#. ``LClick`` on pad
#. ``RClick`` > Add Via at SMD

.. hint::
  To enable via at SMD, via to pad distance for the same net should be zero.


Bus Route
----------------------------------------
1. Rclick > Select Pins/Vias/Tacks
2. Select pins to be routed together
3. RClick > Bus Route

.. hint::
  If one of the traces in cannot be routed, it will ask you to route it separately.

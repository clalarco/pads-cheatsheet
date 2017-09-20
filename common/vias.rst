****************************************
Vias
****************************************

.. note::

    - **Pad stack** The via shape in the layers
    - **Via Span** The default via used to pass from one layer to another
    - **Through Via** via crossing all layers
    - **Partial Via** Via crossing a only some layers (blind and buried vias)


========================================
Setup
========================================

Set via Pad Stacks
----------------------------------------
#. In Layout (|i-pads-layout|) Setup > Pad Stacks
#. Set Pad Stack type to Via
#. Select Via and change properties

Add a via padstack
----------------------------------------
#. In Pad Stacks dialog, set Via type and Click in 'Add Via'.
#. Select through or partial
#. Set start an end layer for partial vias
#. Set pad styles for Pad and thermal

Set default vias
----------------------------------------

.. only:: pads_std_plus

    #. In Layout (|i-pads-layout|) Setup > Via Spans
    #. Set Default via for the given according to vias types and layers


.. only:: pads_maker

    #. Setup > Design Rules... > Default > Routing
    #. At Vias section, select vias (selected = enabled)


.. only:: pads_std_plus

    Set vias per Layer/Class
    ----------------------------------------
    In Constraint manager (|i-constraint-manager|) > Net Classes, set Via Assignments (same dialog as Via Spans)


.. only:: pads_std_plus

    ========================================
    Stitching vias
    ========================================

    Setup
    ----------------------------------------
    #. In Layout (|i-pads-layout|) Tools > Options, Via Patterns page
    #. Choose GND at 'Add vias from net' option.
    #. Choose Via type
    #. For shapes, select Net and Via type if required

    Add Stitching vias around nets
    ----------------------------------------
    #. ``RClick`` > Select Nets
    #. Choose nets
    #. ``RClick`` > Add Via Shield
    #. ESC
    #. ``RClick`` > Select Pins/Vias/Tacks
    #. Move/remove the unwanted vias

    Fill a shape with stitching vias
    ----------------------------------------
    #. Choose a 'solid copper' shape (|il-drafting| > |il-solid-copper|)
    #. ``RClick`` > Select Shapes
    #. Select shape
    #. ``RClick`` > Via Stitch

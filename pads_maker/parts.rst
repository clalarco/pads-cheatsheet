****************************************
Parts
****************************************

========================================
Symbols
========================================

.. hint::
    Use PADS Maker Schematic |i-pads-maker-schematic|

New Symbol
----------------------------------------
In an existing design: File > New > Symbol

New Symbol (box type)
----------------------------------------
#. Create csv from template
#. In an existing design: File > New > Symbol from Pin List

.. hint::
    Check wiki help "Creating and Editing Parts/Symbols", Method #3 for excel template

========================================
Symbols
========================================

.. hint::
    Use PADS Maker Layout |i-pads-maker-layout|

Add a Decal
----------------------------------------
#. Select decals section and partition
#. Over Partition ``RClick`` > New Decal...
#. If possible, use Decal Wizard

Use Decal Wizard
----------------------------------------
#. |il-drafting|  > |il-decal-wizard|
#. At bottom, select units
#. Choose type (dual, quad, polar, BGA/PGA)
#. Fill data, click OK.

Add a Part
----------------------------------------
#. Select 'Parts' section and partition
#. Select Logic Family (UND by default)
#. In PCB Decals assign Decals
#. In Gates, Click 'Add' and choose symbol in 'CAE Decal 1', 'CAE Decal 2', etc
#. Make a copy of C:\PADS Projects\Samples\Part_Pins_Template.csv and complete the info for Pins Tab.
#. In 'Pins' tab, click on Import CSV and import the completed CSV
#. Click 'Check Part' and fix issues before click OK

Part with fractures
----------------------------------------
In Gates Tab, add multiple Gates with Swap 0

Part with multiple symbol representations
-----------------------------------------
Add CAE Decal 1, CAE Decal 2, etc.

Part with duplicate symbols (E.g., a quad nand IC)
--------------------------------------------------
Add many gates with the same swap number, but different to 0

Add data into databook
----------------------------------------
#. Choose partition at Parts section
#. ``RClick`` > Edit parametric data


.. note::
    Pins Tab Information:
        - **Pin Group** Gate A, Gate B, Unused pin or Signal
        - **Number** Decal number
        - **Name** Symbol name
        - **Type** Source, Bidirectional, etc
        - **Swap** Gates Swap groups
        - **Seq** Symbol pin name

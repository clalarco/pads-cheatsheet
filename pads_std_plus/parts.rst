****************************************
Parts
****************************************

.. hint::
    Use Library Tools |i-pads-library-tools|

========================================
New Part
========================================
#. Add symbol
#. Add decal
#. Add part and map symbols and decals

Calling from Schematics
----------------------------------------
Tools > PADS Library Tools

Calling from Layout
----------------------------------------
File > PADS Library Tools

Add a Symbol (box type)
----------------------------------------
#. Select symbols section and partition.
#. Over Partition ``RClick`` > New Symbol or Symbol Wizard
#. Choose Module and Fracture for big pin counts parts. Fill rows.

.. tip::
    You can copy/paste from Excel!

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

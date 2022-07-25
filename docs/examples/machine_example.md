---
hide:
  - toc
---

# machine_controller
## check production list discrepancies

```python 
import machine_controller as mac
import cadwork

btl_enum = 5 # VERSION: "BTL V10.6"
# The enumeration is done according to the machine export listing in the export menu.
file_path   = 'C:\\Downloads\\api_btl.btl'
mac.export_btl(btl_enum, file_path)

```

```python 
import machine_controller as mac
import cadwork

hundegger_enum = 3 # Hundegger K2
# The enumeration is done according to the machine export listing in the export menu.
mac.export_hundegger(hundegger_enum)

```
<noscript>
    <img src="https://analytics.cadwork.ca/ingress/e6b1702b-6224-4e93-94b7-9e4c2cd7ae06/pixel.gif">
</noscript>
<script defer src="https://analytics.cadwork.ca/ingress/e6b1702b-6224-4e93-94b7-9e4c2cd7ae06/script.js"></script>
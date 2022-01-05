# menu_controller
## create a simple cadwork menu 

```python 
import menu_controller as mec 
import utility_controller as uc
import cadwork

menu_options = 'Foo', 'Bar', 'Baz', '', 'Return'

while True:
    menu = mec.display_simple_menu(menu_options)

    if menu == 'Foo':
        uc.print_error('You pressed Foo')
        
    elif menu == 'Bar':
        uc.print_error('You pressed Bar')
        
    elif menu == 'Baz':
        uc.print_error('You pressed Baz')
        
    elif menu == 'Return':
        break

```

Above code generates a menu structure like this.

![Backup Text](../img/menu.png "Example Menu")

<noscript>
    <img src="https://analytics.cadwork.ca/ingress/e6b1702b-6224-4e93-94b7-9e4c2cd7ae06/pixel.gif">
</noscript>
<script defer src="https://analytics.cadwork.ca/ingress/e6b1702b-6224-4e93-94b7-9e4c2cd7ae06/script.js"></script>
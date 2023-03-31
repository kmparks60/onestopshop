                *****SHOP-O-RAMA-PALOOZA*****

At the beginning of the CLI we're greeted with the options of a Guest or Owner login. This is done by an if/elif statement.

If you're a store owner then you can type in your full name and have access to the owner portal. If you're a guest then you simply press the enter button to proceed. 


<<< Owner Portal >>>
WELCOME OWNER
In the owner portal you are greeted with a message that gives you several options.
To add and item to your inventory simply type 'add'.
To view other owners type 'view'.

If the add option is selected:
Add item:
Add price:
Add Store id:
Add Owner id:

Then check onestopshop.db to make sure it is persisited. 

If 'view' option is selected you have the same options as the Guest Portal but with the extra option to add.


<<< Guest Portal >>>
In the guest portal you are greeted with a message that displays a prompt to type 'start' to proceed or 'exit' to exit the CLI.

You are now shown a prompt that offers; 
-To View Selection of Stores type "S" or "s"
-To View Selection of Owners type "O" or "o"

Selecting Stores will show you a list of the stores available for viewing. 
Selecting Owners will show you a list of the owners available for viewing.

If Stores is selceted you can choose which store's inventory to view by entering the Store's id.
After selecting which store you want to view the inventory will be displayed.

If Owners is selected you can choose to view which Stores they own.
After selecting which owner you want to view the list of stores will be displayed.
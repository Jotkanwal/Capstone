   M S B A M L   `   `   `  ���� C  ?TempHost, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null#clr-namespace:TempHostTempHost      TempHost.AdvancedView   \ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     @d2http://schemas.microsoft.com/expression/blend/2008     Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     (localclr-namespace:TempHost       � Title$  Advanced Settings��$	��400��$	��250��.��� -   $��baseGrid��$��10 10 10 10q� � RowDefinitions �� $��20 ��� $
��auto ��� $
��auto ��� $
��auto ��� $
��auto ��� $��20 � � ColumnDefinitions �� $
��auto ��� $
��auto �.+��� -    ��Name$ pnlControls��$��1��$��0��.+��� $��Temp Target:�� �� Target ��  �� ElementName$ 
txtTempSet���� -    ��Name$ 
txtTempSet��$	��100��$��20���� $��Humidity Target:�� �� $ txtHumidSet���� -   $ txtHumidSet��$	��100��$��20���� $�� �� �� $ btnHeaterReset���� -    ��Name$ btnHeaterReset��$	��100��$��20��$��Heater Reset���� $�� �� �� $ 
btnDbReset���� -   $ 
btnDbReset��$	��100��$��20��$��DB Reset���� -   $ pnlReporting��$��1��$��1��.+��� $��Ambient Temperature:�� �� $ txtCurrTemp���� -   $ txtCurrTemp��$	��100��$��20�� �� 
IsReadOnly . �� $��Ambient Humidity:�� �� $ txtCurrHumidity���� -	   $ txtCurrHumidity��$	��100��$��20�� . �� -
   $ 
btnTempLog��$	��100��$��20��$��Temp History��$��0 26 0 0q��� -   $ btnTempSched��$	��100��$��20��$��Temp Schedule��$��0 26 0 0q��� -   $ pnlHistogram��$��2��$��2���� -   $ btnBack��$
��Back��$��4��   SpacedButton#��[  
   M S B A M L   `   `   `  ����C  ?TempHost, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null#clr-namespace:TempHostTempHost  5   	       TempHost.AdvancedView   5   	   \ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5   	   R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5   	   @d2http://schemas.microsoft.com/expression/blend/2008     5   	   Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5   	   (localclr-namespace:TempHost     5   	     � Title$  Advanced Settings��5   	   $	��400��6#   $	��250��60   .��5	      � -   5        $��baseGrid��5	      $��10 10 10 10q�6    � RowDefinitions 5
   
   �� 5      $��20 �6   �� 5      $
��auto �6   �� 5      $
��auto �6   �� 5      $
��auto �6   �� 5      $
��auto �6   �� 5      $��20 �6    � ColumnDefinitions 5   
   �� 5      $
��auto �6   �� 5      $
��auto �6   .+�5   
   �� -   5         ��Name$ pnlControls��5      $��1��6*   $��0��67   .+�5      �� $��Temp Target:��6    �� Target 6+   ��  �� ElementName$ 
txtTempSet���� 5      -   5         ��Name$ 
txtTempSet��5      $	��100��6*   $��20��66   �� 5      $��Humidity Target:��6    6/   �� $ txtHumidSet���� 5      -   5        $ txtHumidSet��5      $	��100��6+   $��20��67   �� 5      $�� ��6    6   �� $ btnHeaterReset���� 5      -   5         ��Name$ btnHeaterReset��5      $	��100��6-   $��20��69   $��Heater Reset��6E   �� 5      $�� ��6    6   �� $ 
btnDbReset���� 5      -   5        $ 
btnDbReset��5      $	��100��6)   $��20��65   $��DB Reset��6A   5       �� 5!   
   -   5        $ pnlReporting��5!      $��1��6+   $��1��68   .+�5"      �� $��Ambient Temperature:��6    63   �� $ txtCurrTemp���� 5#      -   5        $ txtCurrTemp��5#      $	��100��6+   $��20��67    �� 
IsReadOnly . 6C   �� 5$      $��Ambient Humidity:��6    60   �� $ txtCurrHumidity���� 5%      -	   5        $ txtCurrHumidity��5%      $	��100��6/   $��20��6;    . 6G   �� 5&      -
   5        $ 
btnTempLog��5&      $	��100��6)   $��20��65   $��Temp History��6A   $��0 26 0 0q�6q   �� 5'      -   5        $ btnTempSched��5'      $	��100��6+   $��20��67   $��Temp Schedule��6C   $��0 26 0 0q�6w   5(      �� 5)   
   -   5        $ pnlHistogram��5)      $��2��6+   $��2��68   50      �� 51   
   -   5        $ btnBack��51      $
��Back��6"   $��4��6G      SpacedButton#��[  6T   52      54      
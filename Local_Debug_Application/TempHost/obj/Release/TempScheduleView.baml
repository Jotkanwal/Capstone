   M S B A M L   `   `   `  ���� C  ?TempHost, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null#clr-namespace:TempHostTempHost      TempHost.TempScheduleView   \ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     @d2http://schemas.microsoft.com/expression/blend/2008     Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     (localclr-namespace:TempHost       � Title$  TempScheduleView��$	��450��$	��800��.���  � RowDefinitions �� $��20 ��� $
��auto ��� $
��auto ��� $��* ��� $
��auto �.+��� $��1��" Temperature Schedule Maintenance&   System.Windows.Controls.DataGrid  -     Name$ tblTempHistory��$��2��   
IsReadOnly .    CanUserResizeRows .     AutoGenerateColumns .  $��10 10 10 10q�����    Columns 0  *System.Windows.Controls.DataGridTextColumn  ,  &System.Windows.Controls.DataGridColumn   Header$ Temperature��1  +System.Windows.Controls.DataGridBoundColumn   Binding �� *temp+  $ 
Start Time�� �� *	startDate+  $ End Time�� �� *	endDate+  $ Upload Time��	   Width5  /System.Windows.Controls.DataGridLengthConverter$	 *  �� *
uploadDate+4  .System.Windows.Controls.DataGridTemplateColumn  $ Delete��$		 120 
   CellTemplate
 �� .R��� $��Delete��$	��100���� -    ��Name$ btnBack��$
��Back��$��50��$��	0 10 0 10q�$��	10 2 10 2q�$��4��$
��Left=�
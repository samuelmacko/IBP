# Application for presenting a Red Hat Virtualization inventory

## Introduction
__ovirt-inventory__ is an application for easy access to the RHEV inventory.

## Building
To run __ovirt-inventory__, user needs `python3` and `ovirt-engine` repository already installed.
1. User can clone git repository containing source codes from [here](https://github.com/xmacko10/IBP).
	
    In that case, user also needs to install `python3-qt5` and `python3-ovirt-engine-sdk4`.
2. User can use a `RPM` file available [here](https://github.com/xmacko10/IBP) which will install everything needed.

## Usage
### Logging in
After launch, input dialog containing three input fields is displayed.
- __username__ field expecting _username_ and _domain_ in format: `username@domain`
- __password__ field expecting corresponding password
- __url__ field expecting _FQDN_ of the target virtual machine

### Hide/show columns
By checking or unchecking checkboxes in `Select Column` drop-down menu, user can hide or show table columns.

### Refresh
By pressing the _Refresh Button_, user can load up-to-date data.

### Filter
User can write custom filters into a filter field. Filter needs to be in format `column name` `<|>|=` `value`.
Filter supports evaluating multiple filters at the same time. All sub-filters are in `AND` relation and need to be separated from each other by `,`.

### Ordering
User can order items in columns in ascending or descending order by clicking on the column header he wants to order.

### Redirecting
Some table cells contain multiple values (for example one _virtual machine_ can contain multiple _disks_). In that case, cell displays the first item followed by the number in parentheses
expressing how many other items are in that cell. By double clicking such cell, user is redirected to the corresponding tab and right filter is applied.

### Export to .csv
User can export current table into `.csv` file. Go to `File` -> `export`.

### Save
User can save current configuration of all tables into `config` file by going `File` -> `export`.
These information will be saved in a `config` file:
- user name
- domain
- checkboxes from all the tables 

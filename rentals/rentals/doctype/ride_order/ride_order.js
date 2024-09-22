// Copyright (c) 2024, Gharieb Khalifa and contributors
// For license information, please see license.txt

 frappe.ui.form.on("Ride Order", {
     setup(frm) {
        console.log("setup ...")
     },
    onload(frm) {
        console.log("load ...", $('body'))
        
    },
 	refresh(frm) {
        if (frm.doc.status === "New") {
            frm.add_custom_button("Accept", ()=>{
                frm.set_value('status', 'Accepted')
                frm.save()
            }, 'Actions')
            frm.add_custom_button("Rejected", ()=>{
                frm.set_value('status', 'Rejected')
                frm.save()
            }, 'Actions')
        }

 	},
 });

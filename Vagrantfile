# Vars
box = "minimal/centos7"

Vagrant.configure("2") do |config|
  #config.vm.provision "chef_solo" do |chef|
  #  chef.cookbooks_path = "chef-repo/cookbooks"
  #  chef.roles_path = "chef-repo/roles"
  #  chef.data_bags_path = "chef-repo/data_bags"
  #  chef.add_role("base")
  #end
  config.vm.define "proxbox" do |proxbox|
    proxbox.vm.box = "#{box}"
    proxbox.vm.hostname = 'proxbox'
    proxbox.vm.box_url = "#{box}"

    proxbox.vm.network :private_network, ip: "192.168.56.101"

    proxbox.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--memory", 1024]
      v.customize ["modifyvm", :id, "--name", "proxbox"]
    end
  end

  config.vm.define "proxbox2" do |proxbox|
    proxbox.vm.box = "#{box}"
    proxbox.vm.hostname = 'proxbox2'
    proxbox.vm.box_url = "#{box}"

    proxbox.vm.network :private_network, ip: "192.168.56.102"

    proxbox.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--memory", 1024]
      v.customize ["modifyvm", :id, "--name", "proxbox2"]
    end
  end

  config.vm.define "web1" do |web1|
    web1.vm.box = "#{box}"
    web1.vm.hostname = 'web1'
    web1.vm.box_url = "#{box}"

    web1.vm.network :private_network, ip: "192.168.56.103"

    web1.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--memory", 1024]
      v.customize ["modifyvm", :id, "--name", "web1"]
    end
  end
  config.vm.define "web2" do |web2|
    web2.vm.box = "#{box}"
    web2.vm.hostname = 'web2'
    web2.vm.box_url = "#{box}"

    web2.vm.network :private_network, ip: "192.168.56.104"

    web2.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--memory", 1024]
      v.customize ["modifyvm", :id, "--name", "web2"]
    end
  end
end

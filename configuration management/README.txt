Configuration Management Test
=============================

This solutions makes the following assumption:

  * You have ansible or you can install ansible (It's not hard. Really.)

Instructions:

  1) run: 'ansible-playbook configman.yml' from this directory (or it won't find your template)
  2) ???
  3) Profit!

  The way ansible playbooks are designed so long as you properly use the name: option
they are basically self documenting. It's pretty nice and definitely one of the many
features of ansible I enjoy.

  There is an attached file named sample.output which is the results of running this
here in my environment.

  I just randomly picked 'cat /etc/hostname' as a host specific test only to remember
that CentOS/RHEL don't use that file so those hosts failed but the Ubuntu hosts worked.
This actually worked out pretty well as it very clearly shows failure vs success.

  There are two sets of run results in the sample.output file. The first is with no
deployed files on the remote hosts and the second is with them already deployed so
you can see how it doesn't re-deploy the files. It's a shame I couldn't figure out
how to get ansible to keep the color output when redirecting as that is really nice
for seeing what's going on.

Language justification:

  I'm a huge fan of ansible. I'm still not convinced I'd want to run it as the primary
config management tool for an environment, however as a standalone tool it is extremely
useful for doing one off or extremely complex tasks. There is no complex setup required
for it either. You install it onto a computer of your choice (any computer, even your
desktop or laptop) and run it from there. It's also very easy to work with and just
happens to be the only thing I have currently setup in my home environment.  Otherwise
I probably would have used puppet.

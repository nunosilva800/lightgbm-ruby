# dependencies
require "ffi"

# modules
require "lightgbm/utils"
require "lightgbm/booster"
require "lightgbm/dataset"
require "lightgbm/ffi"
require "lightgbm/version"

module LightGBM
  class Error < StandardError; end

  def self.train(params, train_set, num_boost_round: 100, valid_sets: [], valid_names: [])
    booster = Booster.new(params: params, train_set: train_set)
    valid_sets.zip(valid_names) do |data, name|
      booster.add_valid(data, name)
    end
    num_boost_round.times do
      booster.update
    end
    booster
  end
end
